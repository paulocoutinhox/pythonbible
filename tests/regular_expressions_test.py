from __future__ import annotations

import re
from typing import Match

import pythonbible as bible
from pythonbible import regular_expressions


def test_chapter_regular_expression() -> None:
    # given a string with a chapter number
    chapter_string: str = "The chapter number is 132."

    # when evaluating that string against the chapter regular expression
    matches: Match[str] | None = re.search(
        regular_expressions.CHAPTER,
        chapter_string,
    )

    # then the match is found
    assert matches
    assert matches.group(0) == "132"


def test_verse_regular_expression() -> None:
    # given a string with a verse number
    verse_string: str = "The verse number is 25."

    # when evaluating that string against the verse regular expression
    matches: Match[str] | None = re.search(
        regular_expressions.VERSE,
        verse_string,
    )

    # then the match is found
    assert matches
    assert matches.group(0) == "25"


def test_chapter_and_verse_regular_expression() -> None:
    chapter_and_verse_references: list[str] = [
        "1:2",
        "3",
        "142 : 5",
        "43:    324",
    ]

    for reference in chapter_and_verse_references:
        # given a string with a chapter and verse reference
        chapter_and_verse_string: str = (
            f"The chapter and verse reference is {reference}."
        )

        # when evaluating that string against the chapter and verse regular expression
        matches: Match[str] | None = re.search(
            regular_expressions.CHAPTER_AND_VERSE,
            chapter_and_verse_string,
        )

        # then the match is found
        assert matches
        assert matches.group(0) == reference


def test_range_regular_expression() -> None:
    range_references: dict[str, str] = {
        "1:2-3": "-3",
        "3-4": "-4",
        "142 : 5 - 53 : 23": " - 53 : 23",
        "43:    324 - 325": " - 325",
        "Genesis - Deuteronomy": " - Deuteronomy",
        "Genesis 1 - Exodus 2": " - Exodus 2",
        "Genesis 1:1 - Exodus 2:2": " - Exodus 2:2",
    }

    for reference, expected_match in range_references.items():
        # given a string with a chapter range reference
        chapter_range_string: str = f"The chapter range reference is {reference}"

        # when evaluating that string against the chapter range regular expression
        matches: Match[str] | None = re.search(
            regular_expressions.RANGE,
            chapter_range_string,
        )

        # then the match is found
        assert matches
        assert matches.group(0) == expected_match


def test_additional_reference_regular_expression() -> None:
    additional_references: list[str] = [
        "1:2,4",
        "3-4,6",
        "123 : 5 - 13, 16 - 18",
        "32:43-45,54,33:12",
    ]

    for reference in additional_references:
        # given a string with an additional reference
        additional_reference_string: str = f"The additional reference is {reference}."

        # when evaluating that string against the additional reference regular
        # expression
        matches: Match[str] | None = re.search(
            regular_expressions.FULL_CHAPTER_AND_VERSE,
            additional_reference_string,
        )

        # then the match is found
        assert matches
        assert matches.group(0) == reference


def test_multiple_additional_references() -> None:
    # given a string with multiple additional references
    full_string: str = (
        "You should read Matthew 1:18 - 2:18, Luke 3: 5-7, "
        "Psalm 130:4,8 and Jeremiah 29:32-30:10,11"
    )

    # when evaluating that string against the full regular expression
    matches: list[Match[str]] = re.findall(
        regular_expressions.FULL_CHAPTER_AND_VERSE,
        full_string,
    )

    # then the matches are found
    assert len(matches) == 4
    assert matches[0][0] == "1:18 - 2:18"
    assert matches[1][0] == "3: 5-7"
    assert matches[2][0] == "130:4,8"
    assert matches[3][0] == "29:32-30:10,11"


def test_multiple_full_references() -> None:
    # given a string with multiple full scripture references
    full_string: str = (
        "You should read Matthew 1:18 - 2:18, Luke 3: 5-7, "
        "Psalm 130:4,8 and Jeremiah 29:32-30:10,11"
    )

    # when evaluating that string against the full regular expression
    matches: list[Match[str]] = re.findall(
        regular_expressions.SCRIPTURE_REFERENCE_REGULAR_EXPRESSION,
        full_string,
    )

    # then the matches are found
    assert len(matches) == 4
    assert matches[0][0] == "Matthew 1:18 - 2:18"
    assert matches[1][0] == "Luke 3: 5-7"
    assert matches[2][0] == "Psalm 130:4,8"
    assert matches[3][0] == "Jeremiah 29:32-30:10,11"


def test_multiple_full_references_lower_case() -> None:
    # given a lower case string with multiple full scripture references
    full_string: str = (
        "You should read Matthew 1:18 - 2:18, Luke 3: 5-7, "
        "Psalm 130:4,8 and Jeremiah 29:32-30:10,12".lower()
    )

    # when evaluating that string against the full regular expression
    matches: list[Match[str]] = re.findall(
        regular_expressions.SCRIPTURE_REFERENCE_REGULAR_EXPRESSION,
        full_string,
    )

    # then the matches are found
    assert len(matches) == 4
    assert matches[0][0] == "Matthew 1:18 - 2:18".lower()
    assert matches[1][0] == "Luke 3: 5-7".lower()
    assert matches[2][0] == "Psalm 130:4,8".lower()
    assert matches[3][0] == "Jeremiah 29:32-30:10,12".lower()


def test_reference_with_no_verses() -> None:
    # given a string with a reference with no verse numbers
    test_string: str = "The ten commandments can be found in Exodus 20."

    # when evaluating that string against the full regular expression
    matches: list[Match[str]] = re.findall(
        regular_expressions.SCRIPTURE_REFERENCE_REGULAR_EXPRESSION,
        test_string,
    )

    # then the matches are found
    assert len(matches) == 1
    assert matches[0][0] == "Exodus 20"


def test_philemon_not_philippians() -> None:
    # given a string with a Philemon reference
    text: str = "Philemon 1:9"

    # when evaluating the string to see if it matches the Philippians regular expression
    matches: list[Match[str]] = re.findall(
        bible.Book.PHILIPPIANS.regular_expression,
        text,
    )

    # then the matches are not found
    assert not matches

    # when evaluating the string to see if it matches the Philemon regular expression
    matches = re.findall(
        bible.Book.PHILEMON.regular_expression,
        text,
    )

    # then the match is found
    assert len(matches) == 1


def test_cross_book_regex() -> None:
    # given a reference that ranges over multiple books
    text: str = "The books of the law are Genesis - Deuteronomy"

    matches: list[Match[str]] = re.findall(regular_expressions.CROSS_BOOK, text)

    assert len(matches) == 1
    assert matches[0][0] == "Genesis - Deuteronomy"


def test_jo() -> None:
    # "Jo" should match to John, but make sure "Joshua", "Job", and "Jonah" do not
    # match to John

    # given a reference with the abbreviation "Jo"
    text = "Jo 1:1"

    # when evaluating the string to see if it matches the Philemon regular expression
    john_matches = re.findall(
        bible.Book.JOHN.regular_expression,
        text,
    )

    # then the match is found
    assert len(john_matches) == 1

    # given strings that should not match
    test_strings = [
        "Joshua",
        "Job",
        "Jonah",
    ]

    for test_string in test_strings:
        # when evaluating the string to see if it matches the John regular expression
        matches: list[Match[str]] = re.findall(
            bible.Book.JOHN.regular_expression,
            f"{test_string} 1:1",
        )

        # then the matches are not found
        assert not matches


def test_jud() -> None:
    # "Jud" should match to Jude, but make sure "Judges" does not match to Jude

    # given a reference with the abbreviation "Jud"
    text = "Jud 1:1"

    # when evaluating the string to see if it matches the Philemon regular expression
    matches = re.findall(
        bible.Book.JUDE.regular_expression,
        text,
    )

    # then the match is found
    assert len(matches) == 1

    # given a reference that should not match
    # given a reference with the abbreviation "Jud"
    text = "Judges 1:1"

    # when evaluating the string to see if it matches the Philemon regular expression
    matches = re.findall(
        bible.Book.JUDE.regular_expression,
        text,
    )

    # then the match is found
    assert not matches
