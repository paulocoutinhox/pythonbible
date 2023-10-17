from __future__ import annotations

from functools import lru_cache

from pythonbible.books import Book
from pythonbible.errors import InvalidChapterError
from pythonbible.errors import InvalidVerseError

MAX_VERSE_NUMBER_BY_BOOK_AND_CHAPTER: dict[Book, list[int]] = {
    Book.GENESIS: [
        31,
        25,
        24,
        26,
        32,
        22,
        24,
        22,
        29,
        32,
        32,
        20,
        18,
        24,
        21,
        16,
        27,
        33,
        38,
        18,
        34,
        24,
        20,
        67,
        34,
        35,
        46,
        22,
        35,
        43,
        55,
        32,
        20,
        31,
        29,
        43,
        36,
        30,
        23,
        23,
        57,
        38,
        34,
        34,
        28,
        34,
        31,
        22,
        33,
        26,
    ],
    Book.EXODUS: [
        22,
        25,
        22,
        31,
        23,
        30,
        25,
        32,
        35,
        29,
        10,
        51,
        22,
        31,
        27,
        36,
        16,
        27,
        25,
        26,
        36,
        31,
        33,
        18,
        40,
        37,
        21,
        43,
        46,
        38,
        18,
        35,
        23,
        35,
        35,
        38,
        29,
        31,
        43,
        38,
    ],
    Book.LEVITICUS: [
        17,
        16,
        17,
        35,
        19,
        30,
        38,
        36,
        24,
        20,
        47,
        8,
        59,
        57,
        33,
        34,
        16,
        30,
        37,
        27,
        24,
        33,
        44,
        23,
        55,
        46,
        34,
    ],
    Book.NUMBERS: [
        54,
        34,
        51,
        49,
        31,
        27,
        89,
        26,
        23,
        36,
        35,
        16,
        33,
        45,
        41,
        50,
        13,
        32,
        22,
        29,
        35,
        41,
        30,
        25,
        18,
        65,
        23,
        31,
        40,
        16,
        54,
        42,
        56,
        29,
        34,
        13,
    ],
    Book.DEUTERONOMY: [
        46,
        37,
        29,
        49,
        33,
        25,
        26,
        20,
        29,
        22,
        32,
        32,
        18,
        29,
        23,
        22,
        20,
        22,
        21,
        20,
        23,
        30,
        25,
        22,
        19,
        19,
        26,
        68,
        29,
        20,
        30,
        52,
        29,
        12,
    ],
    Book.JOSHUA: [
        18,
        24,
        17,
        24,
        15,
        27,
        26,
        35,
        27,
        43,
        23,
        24,
        33,
        15,
        63,
        10,
        18,
        28,
        51,
        9,
        45,
        34,
        16,
        33,
    ],
    Book.JUDGES: [
        36,
        23,
        31,
        24,
        31,
        40,
        25,
        35,
        57,
        18,
        40,
        15,
        25,
        20,
        20,
        31,
        13,
        31,
        30,
        48,
        25,
    ],
    Book.RUTH: [
        22,
        23,
        18,
        22,
    ],
    Book.SAMUEL_1: [
        28,
        36,
        21,
        22,
        12,
        21,
        17,
        22,
        27,
        27,
        15,
        25,
        23,
        52,
        35,
        23,
        58,
        30,
        24,
        42,
        15,
        23,
        29,
        22,
        44,
        25,
        12,
        25,
        11,
        31,
        13,
    ],
    Book.SAMUEL_2: [
        27,
        32,
        39,
        12,
        25,
        23,
        29,
        18,
        13,
        19,
        27,
        31,
        39,
        33,
        37,
        23,
        29,
        33,
        43,
        26,
        22,
        51,
        39,
        25,
    ],
    Book.KINGS_1: [
        53,
        46,
        28,
        34,
        18,
        38,
        51,
        66,
        28,
        29,
        43,
        33,
        34,
        31,
        34,
        34,
        24,
        46,
        21,
        43,
        29,
        53,
    ],
    Book.KINGS_2: [
        18,
        25,
        27,
        44,
        27,
        33,
        20,
        29,
        37,
        36,
        21,
        21,
        25,
        29,
        38,
        20,
        41,
        37,
        37,
        21,
        26,
        20,
        37,
        20,
        30,
    ],
    Book.CHRONICLES_1: [
        54,
        55,
        24,
        43,
        26,
        81,
        40,
        40,
        44,
        14,
        47,
        40,
        14,
        17,
        29,
        43,
        27,
        17,
        19,
        8,
        30,
        19,
        32,
        31,
        31,
        32,
        34,
        21,
        30,
    ],
    Book.CHRONICLES_2: [
        17,
        18,
        17,
        22,
        14,
        42,
        22,
        18,
        31,
        19,
        23,
        16,
        22,
        15,
        19,
        14,
        19,
        34,
        11,
        37,
        20,
        12,
        21,
        27,
        28,
        23,
        9,
        27,
        36,
        27,
        21,
        33,
        25,
        33,
        27,
        23,
    ],
    Book.EZRA: [
        11,
        70,
        13,
        24,
        17,
        22,
        28,
        36,
        15,
        44,
    ],
    Book.NEHEMIAH: [
        11,
        20,
        32,
        23,
        19,
        19,
        73,
        18,
        38,
        39,
        36,
        47,
        31,
    ],
    Book.ESTHER: [
        22,
        23,
        15,
        17,
        14,
        14,
        10,
        17,
        32,
        3,
    ],
    Book.JOB: [
        22,
        13,
        26,
        21,
        27,
        30,
        21,
        22,
        35,
        22,
        20,
        25,
        28,
        22,
        35,
        22,
        16,
        21,
        29,
        29,
        34,
        30,
        17,
        25,
        6,
        14,
        23,
        28,
        25,
        31,
        40,
        22,
        33,
        37,
        16,
        33,
        24,
        41,
        30,
        24,
        34,
        17,
    ],
    Book.PSALMS: [
        6,
        12,
        8,
        8,
        12,
        10,
        17,
        9,
        20,
        18,
        7,
        8,
        6,
        7,
        5,
        11,
        15,
        50,
        14,
        9,
        13,
        31,
        6,
        10,
        22,
        12,
        14,
        9,
        11,
        12,
        24,
        11,
        22,
        22,
        28,
        12,
        40,
        22,
        13,
        17,
        13,
        11,
        5,
        26,
        17,
        11,
        9,
        14,
        20,
        23,
        19,
        9,
        6,
        7,
        23,
        13,
        11,
        11,
        17,
        12,
        8,
        12,
        11,
        10,
        13,
        20,
        7,
        35,
        36,
        5,
        24,
        20,
        28,
        23,
        10,
        12,
        20,
        72,
        13,
        19,
        16,
        8,
        18,
        12,
        13,
        17,
        7,
        18,
        52,
        17,
        16,
        15,
        5,
        23,
        11,
        13,
        12,
        9,
        9,
        5,
        8,
        28,
        22,
        35,
        45,
        48,
        43,
        13,
        31,
        7,
        10,
        10,
        9,
        8,
        18,
        19,
        2,
        29,
        176,
        7,
        8,
        9,
        4,
        8,
        5,
        6,
        5,
        6,
        8,
        8,
        3,
        18,
        3,
        3,
        21,
        26,
        9,
        8,
        24,
        13,
        10,
        7,
        12,
        15,
        21,
        10,
        20,
        14,
        9,
        6,
    ],
    Book.PROVERBS: [
        33,
        22,
        35,
        27,
        23,
        35,
        27,
        36,
        18,
        32,
        31,
        28,
        25,
        35,
        33,
        33,
        28,
        24,
        29,
        30,
        31,
        29,
        35,
        34,
        28,
        28,
        27,
        28,
        27,
        33,
        31,
    ],
    Book.ECCLESIASTES: [
        18,
        26,
        22,
        16,
        20,
        12,
        29,
        17,
        18,
        20,
        10,
        14,
    ],
    Book.SONG_OF_SONGS: [
        17,
        17,
        11,
        16,
        16,
        13,
        13,
        14,
    ],
    Book.ISAIAH: [
        31,
        22,
        26,
        6,
        30,
        13,
        25,
        22,
        21,
        34,
        16,
        6,
        22,
        32,
        9,
        14,
        14,
        7,
        25,
        6,
        17,
        25,
        18,
        23,
        12,
        21,
        13,
        29,
        24,
        33,
        9,
        20,
        24,
        17,
        10,
        22,
        38,
        22,
        8,
        31,
        29,
        25,
        28,
        28,
        25,
        13,
        15,
        22,
        26,
        11,
        23,
        15,
        12,
        17,
        13,
        12,
        21,
        14,
        21,
        22,
        11,
        12,
        19,
        12,
        25,
        24,
    ],
    Book.JEREMIAH: [
        19,
        37,
        25,
        31,
        31,
        30,
        34,
        22,
        26,
        25,
        23,
        17,
        27,
        22,
        21,
        21,
        27,
        23,
        15,
        18,
        14,
        30,
        40,
        10,
        38,
        24,
        22,
        17,
        32,
        24,
        40,
        44,
        26,
        22,
        19,
        32,
        21,
        28,
        18,
        16,
        18,
        22,
        13,
        30,
        5,
        28,
        7,
        47,
        39,
        46,
        64,
        34,
    ],
    Book.LAMENTATIONS: [
        22,
        22,
        66,
        22,
        22,
    ],
    Book.EZEKIEL: [
        28,
        10,
        27,
        17,
        17,
        14,
        27,
        18,
        11,
        22,
        25,
        28,
        23,
        23,
        8,
        63,
        24,
        32,
        14,
        49,
        32,
        31,
        49,
        27,
        17,
        21,
        36,
        26,
        21,
        26,
        18,
        32,
        33,
        31,
        15,
        38,
        28,
        23,
        29,
        49,
        26,
        20,
        27,
        31,
        25,
        24,
        23,
        35,
    ],
    Book.DANIEL: [
        21,
        49,
        30,
        37,
        31,
        28,
        28,
        27,
        27,
        21,
        45,
        13,
    ],
    Book.HOSEA: [
        11,
        23,
        5,
        19,
        15,
        11,
        16,
        14,
        17,
        15,
        12,
        14,
        16,
        9,
    ],
    Book.JOEL: [
        20,
        32,
        21,
    ],
    Book.AMOS: [
        15,
        16,
        15,
        13,
        27,
        14,
        17,
        14,
        15,
    ],
    Book.OBADIAH: [
        21,
    ],
    Book.JONAH: [
        17,
        10,
        10,
        11,
    ],
    Book.MICAH: [
        16,
        13,
        12,
        13,
        15,
        16,
        20,
    ],
    Book.NAHUM: [
        15,
        13,
        19,
    ],
    Book.HABAKKUK: [
        17,
        20,
        19,
    ],
    Book.ZEPHANIAH: [
        18,
        15,
        20,
    ],
    Book.HAGGAI: [
        15,
        23,
    ],
    Book.ZECHARIAH: [
        21,
        13,
        10,
        14,
        11,
        15,
        14,
        23,
        17,
        12,
        17,
        14,
        9,
        21,
    ],
    Book.MALACHI: [
        14,
        17,
        18,
        6,
    ],
    Book.MATTHEW: [
        25,
        23,
        17,
        25,
        48,
        34,
        29,
        34,
        38,
        42,
        30,
        50,
        58,
        36,
        39,
        28,
        27,
        35,
        30,
        34,
        46,
        46,
        39,
        51,
        46,
        75,
        66,
        20,
    ],
    Book.MARK: [
        45,
        28,
        35,
        41,
        43,
        56,
        37,
        38,
        50,
        52,
        33,
        44,
        37,
        72,
        47,
        20,
    ],
    Book.LUKE: [
        80,
        52,
        38,
        44,
        39,
        49,
        50,
        56,
        62,
        42,
        54,
        59,
        35,
        35,
        32,
        31,
        37,
        43,
        48,
        47,
        38,
        71,
        56,
        53,
    ],
    Book.JOHN: [
        51,
        25,
        36,
        54,
        47,
        71,
        53,
        59,
        41,
        42,
        57,
        50,
        38,
        31,
        27,
        33,
        26,
        40,
        42,
        31,
        25,
    ],
    Book.ACTS: [
        26,
        47,
        26,
        37,
        42,
        15,
        60,
        40,
        43,
        48,
        30,
        25,
        52,
        28,
        41,
        40,
        34,
        28,
        41,
        38,
        40,
        30,
        35,
        27,
        27,
        32,
        44,
        31,
    ],
    Book.ROMANS: [
        32,
        29,
        31,
        25,
        21,
        23,
        25,
        39,
        33,
        21,
        36,
        21,
        14,
        23,
        33,
        27,
    ],
    Book.CORINTHIANS_1: [
        31,
        16,
        23,
        21,
        13,
        20,
        40,
        13,
        27,
        33,
        34,
        31,
        13,
        40,
        58,
        24,
    ],
    Book.CORINTHIANS_2: [
        24,
        17,
        18,
        18,
        21,
        18,
        16,
        24,
        15,
        18,
        33,
        21,
        14,
    ],
    Book.GALATIANS: [
        24,
        21,
        29,
        31,
        26,
        18,
    ],
    Book.EPHESIANS: [
        23,
        22,
        21,
        32,
        33,
        24,
    ],
    Book.PHILIPPIANS: [
        30,
        30,
        21,
        23,
    ],
    Book.COLOSSIANS: [
        29,
        23,
        25,
        18,
    ],
    Book.THESSALONIANS_1: [
        10,
        20,
        13,
        18,
        28,
    ],
    Book.THESSALONIANS_2: [
        12,
        17,
        18,
    ],
    Book.TIMOTHY_1: [
        20,
        15,
        16,
        16,
        25,
        21,
    ],
    Book.TIMOTHY_2: [
        18,
        26,
        17,
        22,
    ],
    Book.TITUS: [
        16,
        15,
        15,
    ],
    Book.PHILEMON: [
        25,
    ],
    Book.HEBREWS: [
        14,
        18,
        19,
        16,
        14,
        20,
        28,
        13,
        28,
        39,
        40,
        29,
        25,
    ],
    Book.JAMES: [
        27,
        26,
        18,
        17,
        20,
    ],
    Book.PETER_1: [
        25,
        25,
        22,
        19,
        14,
    ],
    Book.PETER_2: [
        21,
        22,
        18,
    ],
    Book.JOHN_1: [
        10,
        29,
        24,
        21,
        21,
    ],
    Book.JOHN_2: [
        13,
    ],
    Book.JOHN_3: [
        14,
    ],
    Book.JUDE: [
        25,
    ],
    Book.REVELATION: [
        20,
        29,
        22,
        11,
        14,
        17,
        17,
        13,
        21,
        11,
        19,
        17,
        18,
        20,
        8,
        21,
        18,
        24,
        21,
        15,
        27,
        21,
    ],
    Book.ESDRAS_1: [
        55,
        25,
        23,
        63,
        70,
        33,
        15,
        92,
        55,
    ],
    Book.TOBIT: [
        22,
        14,
        17,
        21,
        22,
        18,
        16,
        21,
        6,
        13,
        18,
        22,
        18,
        15,
    ],
    Book.WISDOM_OF_SOLOMON: [
        16,
        24,
        19,
        20,
        23,
        25,
        30,
        21,
        18,
        21,
        26,
        27,
        19,
        31,
        19,
        29,
        21,
        25,
        22,
    ],
    Book.ECCLESIASTICUS: [
        30,
        18,
        31,
        31,
        15,
        37,
        36,
        19,
        18,
        31,
        34,
        18,
        26,
        27,
        20,
        30,
        32,
        33,
        30,
        31,
        28,
        27,
        27,
        34,
        26,
        29,
        30,
        26,
        28,
        25,
        31,
        24,
        33,
        31,
        26,
        31,
        31,
        34,
        35,
        30,
        22,
        25,
        33,
        23,
        26,
        20,
        25,
        25,
        16,
        29,
        30,
    ],
    Book.MACCABEES_1: [
        64,
        70,
        60,
        61,
        68,
        63,
        50,
        32,
        73,
        89,
        74,
        53,
        53,
        49,
        41,
        24,
    ],
    Book.MACCABEES_2: [
        36,
        32,
        40,
        50,
        27,
        31,
        42,
        36,
        29,
        38,
        38,
        45,
        26,
        46,
        39,
    ],
}

BOOK_PLACE = 1000000
CHAPTER_PLACE = 1000


@lru_cache()
def __generate_verse_ids() -> tuple[int, ...]:
    return tuple(
        int(
            f"{str(book.value).zfill(2)}"
            f"{str(chapter + 1).zfill(3)}"
            f"{str(verse + 1).zfill(3)}",
        )
        for book, chapters in MAX_VERSE_NUMBER_BY_BOOK_AND_CHAPTER.items()
        for chapter, max_verse in enumerate(chapters)
        for verse in range(max_verse)
    )


VERSE_IDS: tuple[int, ...] = __generate_verse_ids()


@lru_cache()
def get_number_of_chapters(book: Book) -> int:
    """Return the number of chapters in a Book of the Bible.

    :param book: a book of the Bible
    :type book: Book
    :return: the number of chapters in the given book of the Bible
    :rtype: int
    """
    return len(MAX_VERSE_NUMBER_BY_BOOK_AND_CHAPTER[book])


@lru_cache()
def is_single_chapter_book(book: Book) -> bool:
    return get_number_of_chapters(book) == 1


@lru_cache()
def get_number_of_verses(book: Book, chapter: int) -> int:
    """Return the number of verses in a Book and chapter.

    :param book: a book of the Bible
    :type book: Book
    :param chapter: a chapter of the given book of the Bible
    :type chapter: int
    :return: the number of verses in the given book and chapter
    :rtype: int
    :raises InvalidChapterError: if the given chapter isn't a valid chapter for the
                                 given book
    """
    chapter_list: list[int] = MAX_VERSE_NUMBER_BY_BOOK_AND_CHAPTER[book]

    try:
        return chapter_list[chapter - 1]
    except IndexError as error:
        error_message = (
            f"{chapter} is not a valid chapter number for the book of {book.title}. "
            f"Valid chapter numbers are 1-{len(chapter_list)}."
        )
        raise InvalidChapterError(error_message) from error


@lru_cache()
def get_verse_id(book: Book, chapter: int, verse: int) -> int:
    """Return the verse id for the given Book, chapter number, and verse number.

    :param book: a book of the Bible
    :type book: Book
    :param chapter: a chapter number for the given book of the Bible
    :type chapter: int
    :param verse: a verse number for the given book and chapter
    :type verse: int
    :return: the verse id for the given book, chapter, and verse
    :rtype: int
    :raises InvalidVerseError: if the verse doesn't exist for the given book, chapter,
                               and verse
    """
    max_verse_number: int | None = get_number_of_verses(book, chapter)

    if max_verse_number and not 1 <= verse <= max_verse_number:
        error_message = (
            f"{book.title} {chapter}:{verse} is not a valid Bible verse. "
            f"Valid verses for that book and chapter are 1-{max_verse_number}"
        )
        raise InvalidVerseError(error_message)

    return book.value * BOOK_PLACE + chapter * CHAPTER_PLACE + verse


@lru_cache()
def get_book_chapter_verse(verse_id: int) -> tuple[Book, int, int]:
    """Return the Book, chapter number, and verse number for the given verse id.

    :param verse_id: a verse id
    :type verse_id: int
    :return: A tuple containing the Book, chapter number, and verse number for the
             given verse id
    :rtype: tuple[Book, int, int]
    :raises InvalidVerseError: if the verse id does not correspond to a valid verse
    """
    if verse_id not in VERSE_IDS:
        raise InvalidVerseError(verse_id=verse_id)

    return (
        Book(get_book_number(verse_id)),  # type: ignore[call-arg]
        get_chapter_number(verse_id),
        get_verse_number(verse_id),
    )


@lru_cache()
def get_book_number(verse_id: int) -> int:
    """Return the book number for the given verse id.

    :param verse_id: a verse id
    :type verse_id: int
    :return: The book number for the given verse id
    :rtype: int
    """
    return verse_id // BOOK_PLACE


@lru_cache()
def get_chapter_number(verse_id: int) -> int:
    """Return the chapter number for the given verse id.

    :param verse_id: a verse id
    :type verse_id: int
    :return: The chapter number for the given verse id
    :rtype: int
    """
    return verse_id % BOOK_PLACE // CHAPTER_PLACE


@lru_cache()
def get_verse_number(verse_id: int) -> int:
    """Return the verse number for the given verse id.

    :param verse_id: a verse id
    :type verse_id: int
    :return: The verse number for the given verse id
    :rtype: int
    """
    return verse_id % CHAPTER_PLACE
