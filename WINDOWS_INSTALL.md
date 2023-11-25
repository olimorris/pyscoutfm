# Windows Install

Trying to install Python for the first time can feel messy but thankfully it's a one-time exercise if you follow the steps below:

1. Open up a Command Prompt and type `python -V`. You'll need to install Python if you see the below message:

<img src="https://github.com/olimorris/PyScoutFM/assets/9512444/10c7fa7c-fc82-45c5-9740-f3b6b47edc82">

2. Thankfully, type `python` again into the Command Prompt to be taken to the Microsoft Store where it can be installed automatically.
3. Now we can install PyScoutFM with:

```
pip install pyscoutfm
```

4. If you run `pyscoutfm -V` and receive an error, then you need to add python to your [PATH](https://en.wikipedia.org/wiki/PATH_(variable)) environment variable
5. Open up the start menu and type `enviro` and you should see the following match:

<img src="https://github.com/olimorris/PyScoutFM/assets/9512444/c2f8e5a6-0b75-4dd8-af74-bc5d372f0ffb">

6. Press enter and in the following window press the `Environment Variables` button:

<img src="https://github.com/olimorris/PyScoutFM/assets/9512444/ded21f08-8fc1-49f1-89ad-8105e734b98b">

7. Click on the `Path` variable and press `Edit`:

<img src="https://github.com/olimorris/PyScoutFM/assets/9512444/df47c429-ec94-4d49-bd5d-497ecbd66baa">

8. We will now enter in the path to the location of where Python was installed. The easiest way to do that is by typing in `pip show -f pyscoutfm`, after which you'll see the following output:

<img src="https://github.com/olimorris/PyScoutFM/assets/9512444/907ebcbe-0552-4192-8caf-19ee71c4f3aa">

9. Everything up to and NOT INCLUDING `site-packages` is what we're interested in. So copy that and add it as a new environment variable but make sure to add `\Scripts` to the end:

<img src="https://github.com/olimorris/PyScoutFM/assets/9512444/6d4fa4d8-0897-4d67-bea0-5d6b06bc41ef">

10. Now `OK` out of all of the boxes
11. Close and re-open the Command Prompt
12. And type `pyscoutfm -V` to see:

<img src="https://github.com/olimorris/PyScoutFM/assets/9512444/47046274-a294-45b3-8961-aee2a24a7107">

**You're now ready to start using PyScoutFM!!!**

13. Finally, remember to keep PyScoutFM up to date by running `pip install pyscoutfm --upgrade`
