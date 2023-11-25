import pandas as pd


class Data:
    """
    Load the config data and subsequent files
    """

    def __init__(self, export, config):
        self.export = pd.read_html(
            export, header=0, encoding="UTF-8", keep_default_na=False
        )[0]
        self.config = config

    def pre_processing_fixes(self, weightings):
        # Fix nationality
        self.export.rename(columns={"Nat": "1st Nat", "Nat.1": "Nat"})

        # Calculate feet scores
        self.export["Lft"] = self.export["Left Foot"].map(weightings["feet"])
        self.export["Rft"] = self.export["Right Foot"].map(weightings["feet"])
        self.export["Feet"] = self.export["Lft"] + self.export["Rft"]

    def post_processing_fixes(self, weightings):
        output = self.export[
            [col for col in self.config["output_columns"] if col in self.export.columns]
        ]

        # Append the calculated columns to the output
        for key, data in weightings[self.config["weightings_set"]].items():
            score_column = self.calculator(key, data)

            # Append the calculate columns to the output
            output = output.join(score_column.to_frame())

        # Calculate the best position and best rating
        weighting_keys = list(
            {
                key.upper(): data
                for key, data in weightings[self.config["weightings_set"]].items()
            }.keys()
        )
        calculated_cols = output[weighting_keys]

        # Get the column label with the maximum value for each row
        max_columns_per_row = calculated_cols.idxmax(axis=1)

        output["BEST POS"] = max_columns_per_row
        output["BEST RATING"] = output.apply(lambda row: row[row["BEST POS"]], axis=1)

        return output

    def calculator(
        self,
        weightings_key,
        weightings_data,
    ):
        df = self.export.copy()

        # Filter the dataframe for eligible players eligible based on their position
        positions = weightings_data["positions"]
        eligible_players = df["Position"].apply(
            lambda x: any(pos in x for pos in positions)
        )

        # Filter and convert the weightings to a decimal
        att_weightings = {
            k: v / 100
            for k, v in weightings_data["weightings"].items()
            if v >= self.config["filter_values_below"]
        }

        theoretical_max_score = sum(value for value in att_weightings.values()) * 20

        df[weightings_key.upper()] = 0.0

        for attr, scale in att_weightings.items():
            if attr in df.columns:
                # Get explicit with types to prevent warnings in Pandas
                df[attr] = df[attr].astype(float)

                # Calculate the attribute weightings
                df.loc[eligible_players, attr] = (
                    pd.to_numeric(df.loc[eligible_players, attr], errors="coerce")
                    * scale
                )

        # Convert the attribute weightings to a percentage
        df.loc[eligible_players, weightings_key.upper()] = (
            df.loc[eligible_players, att_weightings.keys()].sum(axis=1)
            / theoretical_max_score
            * 100
        )

        return df[weightings_key.upper()].round(2).astype(float)
