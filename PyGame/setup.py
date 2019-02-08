import cx_Freeze
executables = [cx_Freeze.Executable("pygameVideo15.py")]

cx_Freeze.setup(
    name="A bit racey",
    options={"build_exe": {"packages":["pygame"],
                          "include_files":["eddy.png"]}},
    executables=executables
    )
