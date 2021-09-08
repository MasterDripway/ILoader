# ILoader
Python based script utility loader


# Usage

To create a "mod" file, clone the repository and add it to ./mods.

After the file is created, you can set `exclude` in `Main.py` to the files you want excluded from the auto runner.

# How to run a file via runner

All you have to do is create a function `start` much like a main function, which will be automatically run once loaded.

# Performance Indicators - Windows only (for now)

You can enable performance stats via `ILoader.getReourceValues()` and completely disable them with  `ILoader.disablePerformanceStats()`.

This will show your cpu and memory usage if left enabled.
