with open("README.md", "w+") as f:
    f.write("# AP Research: Natural Language Generation Models\n\n"
            "All text samples used in the research are included on this page.\n")

    for folder in range(1, 6):
        for fname in ["ha", "hb", "mc", "mo"]:
            try:
                with open(f'SampleSources/{folder}/{fname}.txt') as g:
                    f.write("\n`")
                    f.write(g.readlines()[0])
                    f.write("`\n")
            except FileNotFoundError:
                print(f'SampleSources/{folder}/{fname}.txt missing')