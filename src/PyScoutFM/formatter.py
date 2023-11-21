class Formatter:
    """
    Format a dataframe
    """

    def __init__(self, df):
        self.df = df

    def to_html(self):
        table = self.df.to_html(
            table_id="fm_data", index=False, classes="display nowrap"
        )

        html = f"""
        <html>
            <head>
                <meta charset="UTF-8">
                <title>PyScoutFM</title>
                <link rel="stylesheet" href="https://cdn.datatables.net/1.13.6/css/jquery.dataTables.min.css">
                <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
                <style>
                    body {{
                        font-family: 'Roboto', sans-serif;
                    }}
                    #fm_data, #fm_data th, #fm_data td {{
                        border: none !important;
                    }}
                </style>
            </head>
            <body>
                <h1>PyScoutFM - Scout Report</h1>
                <div>
                {table}
                </div>
                <script type="text/javascript" src="https://code.jquery.com/jquery-3.7.1.slim.min.js" integrity="sha256-kmHvs0B+OpCW5GVHUNjv9rOmY0IvSIRcf7zGUDTDQM8=" crossorigin="anonymous"></script>
                <script type="text/javascript" src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js"></script>
                <script type="text/javascript">
                    new DataTable('#fm_data', {{
                        pageLength: 25
                    }});
                </script>
            </body>
        </html>
        """

        return html
