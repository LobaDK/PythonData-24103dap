#!/usr/bin/env python3


def word_frequencies(
    filename: str = "/home/lobadk/Documents/PythonData-24103dap/øvelser/e24_word_frequencies/src/alice.txt",
) -> dict[str, int]:
    word_count: dict[str, int] = {}

    with open(file=filename, mode="r") as read:
        for line in read.readlines():
            for word in line.split():
                word = word.strip("""!"#$%&'()*,-./:;?@[]_""")

                word_key: int | None = word_count.get(word, None)

                if word_key is None:
                    word_count[word] = 1
                else:
                    word_count[word] += 1

    return dict(sorted(word_count.items(), key=lambda x: x[1], reverse=True))


def main() -> None:
    print(word_frequencies())


if __name__ == "__main__":
    main()
