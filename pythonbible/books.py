from __future__ import annotations

from enum import Enum
from typing import Any
from typing import Type


def _build_book_regular_expression(
    book: str,
    prefix: str | None = None,
    suffix: str | None = None,
) -> str:
    return _add_suffix(_add_prefix(book, prefix), suffix)


def _add_prefix(regex: str, prefix: str | None = None) -> str:
    return regex if prefix is None else rf"(?:{prefix})(?:\s)?{regex}"


def _add_suffix(regex: str, suffix: str | None = None) -> str:
    return regex if suffix is None else rf"{regex}(?:\s*{suffix})?"


_SAMUEL_REGULAR_EXPRESSION = r"(Samuel|Sam\.*|Sa\.*|Sm\.*)"
_KINGS_REGULAR_EXPRESSION = r"(Kings|Kgs\.*|Kin\.*|Ki\.*|Reyes|Reis|Re\.*|Rs\.*)"
_CHRONICLES_REGULAR_EXPRESSION = r"(Chronicles|Chron\.*|Chro\.*|Chr\.*|Crónicas|Crônicas|Cr\.*)"
_JOHN_REGULAR_EXPRESSION = r"(John|Joh\.*|Jhn\.*|Jo\.*(?!shua|b|nah|el)|Jn\.*|Juan|João|Jn\.*)"
_CORINTHIANS_REGULAR_EXPRESSION = r"(Corinthians|Corintios|Coríntios|Co\.*)"
_THESSALONIANS_REGULAR_EXPRESSION = r"(Thessalonians|Tesalonicenses|Tessalonicenses|Th\.*|Ts\.*)"
_TIMOTHY_REGULAR_EXPRESSION = r"(Timothy|Timoteo|Timóteo|Ti\.*|Tm\.*)"
_PETER_REGULAR_EXPRESSION = r"(Peter|Pedro|Pe\.*|Pt\.*)"

_MACCABEES_REGULAR_EXPRESSION = r"(Maccabees|Macabeos|Macabeus|Ma\.*|M\.*)"

_FIRST = r"1|I\s+|1st\s+|First\s+|Primero\s+|Primeiro\s+|1\s+"
_SECOND = r"2|II|2nd\s+|Second\s+|Segundo\s+|2\s+"
_THIRD = r"3|III|3rd\s+|Third\s+|Tercero\s+|Terceiro\s+|3\s+"

_FIRST_BOOK = rf"{_FIRST}|(First\s+Book\s+of(?:\s+the)?)"
_SECOND_BOOK = rf"{_SECOND}|(Second\s+Book\s+of(?:\s+the)?)"

_EPISTLE_OF_PAUL_TO = r"Epistle\s+of\s+Paul\s+(?:the\s+Apostle\s+)?to(?:\s+the)?"
_GENERAL_EPISTLE_OF = r"(?:General\s+)?Epistle\s+(?:General\s+)?of"

_FIRST_PAUL_EPISTLE = rf"{_FIRST}|(First\s+{_EPISTLE_OF_PAUL_TO})"
_SECOND_PAUL_EPISTLE = rf"{_SECOND}|(Second\s+{_EPISTLE_OF_PAUL_TO})"

_FIRST_GENERAL_EPISTLE = rf"{_FIRST}|(First\s+{_GENERAL_EPISTLE_OF})"
_SECOND_GENERAL_EPISTLE = rf"{_SECOND}|(Second\s+{_GENERAL_EPISTLE_OF})"
_THIRD_GENERAL_EPISTLE = rf"{_THIRD}|(Third\s+{_GENERAL_EPISTLE_OF})"


class Book(Enum):
    """Book is an Enum that contains all the books of the Bible.

    :param name: the unique text identifier of the book
    :type name: str
    :param value: the unique numerical identifier of the book
    :type value: int
    :param title: the common English name of the book
    :type title: str
    :param regular_expression: the regular expression for the book
    :type regular_expression: str
    :param abbreviations: the allowed title abbreviations for the book
    :type abbreviations: tuple[str, ...]
    """

    def __new__(
        cls: Type[Book],
        *args: dict[str, Any],
        **kwargs: dict[str, Any],
    ) -> Book:
        obj: Book = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(
        self: Book,
        _: int,
        title: str,
        regular_expression: str,
        abbreviations: tuple[str, ...],
    ) -> None:
        """Set the title and regular_expression properties."""
        self._title_ = title
        self._regular_expression_ = regular_expression
        self._abbreviations_ = abbreviations

    @property
    def title(self: Book) -> str:
        return self._title_

    @property
    def regular_expression(self: Book) -> str:
        return self._regular_expression_

    @property
    def abbreviations(self: Book) -> tuple[str, ...]:
        return self._abbreviations_

    GENESIS = 1, "Genesis", r"(Gen\.*(?:esis)?|Gén\.*(?:esis)?|Gên\.*(?:esis)?|Gn\.*)", ("Gen", "Gn")
    EXODUS = 2, "Exodus", r"(Exo\.*(?:d\.*)?(?:us)?|Éxo\.*(?:do)?|Êxo\.*(?:do)?|Éx|Êx|Ex\.*)", ("Exo", "Exod", "Éx", "Êx", "Ex")
    LEVITICUS = 3, "Leviticus", r"(Lev\.*(?:iticus)?|Lev\.*(?:ítico)?|Lv\.*)", ("Lev", "Lv")
    NUMBERS = 4, "Numbers", r"(Num\.*(?:bers)?|Num\.*(?:eros)?|Núm\.*|Nm\.*)", ("Num", "Núm", "Nm")
    DEUTERONOMY = 5, "Deuteronomy", r"(Deu\.*(?:t\.*)?(?:eronomy)?|Deu\.*(?:teronomio)?|Dt\.*)", ("Deu", "Deut", "Dt")
    JOSHUA = 6, "Joshua", r"(Joshua|Josh\.*|Jos\.*|Jsh\.*|Josué|Js\.*)", ("Jos", "Jsh", "Josh", "Js")
    JUDGES = 7, "Judges", r"(Judges|Judg\.*|Jdgs\.*|Jdg\.*|Jueces|Jue\.*|Jz\.*)", ("Jdg", "Jdgs", "Judg", "Jue", "Jz")
    RUTH = 8, "Ruth", r"(Ruth|Rut\.*|Rth\.*|Rt\.*)", ("Rth", "Rut", "Rt")
    SAMUEL_1 = (
        9,
        "1 Samuel",
        _build_book_regular_expression(
            _SAMUEL_REGULAR_EXPRESSION,
            prefix=_FIRST_BOOK,
            suffix=r"Otherwise\s+Called\s+The\s+First\s+Book\s+of\s+the\s+Kings",
        ),
        ("Sa", "Sam", "Sm", "1Sm"),
    )
    SAMUEL_2 = (
        10,
        "2 Samuel",
        _build_book_regular_expression(
            _SAMUEL_REGULAR_EXPRESSION,
            prefix=_SECOND_BOOK,
            suffix=r"Otherwise\s+Called\s+The\s+Second\s+Book\s+of\s+the\s+Kings",
        ),
        ("Sa", "Sam", "Sm", "2Sm"),
    )
    KINGS_1 = (
        11,
        "1 Kings",
        _build_book_regular_expression(
            _KINGS_REGULAR_EXPRESSION,
            prefix=_FIRST_BOOK,
            suffix=r"\,\s+Commonly\s+Called\s+the\s+Third\s+Book\s+of\s+the\s+Kings",
        ),
        ("Re", "Rey", "Reis", "Reyes", "Kgs", "Kin", "Ki", "1Rs"),
    )
    KINGS_2 = (
        12,
        "2 Kings",
        _build_book_regular_expression(
            _KINGS_REGULAR_EXPRESSION,
            prefix=_SECOND_BOOK,
            suffix=r"\,\s+Commonly\s+Called\s+the\s+Fourth\s+Book\s+of\s+the\s+Kings",
        ),
        ("Re", "Rey", "Reis", "Reyes", "Kgs", "Kin", "Ki", "2Rs"),
    )
    CHRONICLES_1 = (
        13,
        "1 Chronicles",
        _build_book_regular_expression(
            _CHRONICLES_REGULAR_EXPRESSION,
            prefix=_FIRST_BOOK,
        ),
        ("Cr", "Crón", "Crôn", "Chron", "Chro", "Chr", "1Cr"),
    )
    CHRONICLES_2 = (
        14,
        "2 Chronicles",
        _build_book_regular_expression(
            _CHRONICLES_REGULAR_EXPRESSION,
            prefix=_SECOND_BOOK,
        ),
        ("Cr", "Crón", "Crôn", "Chron", "Chro", "Chr", "2Cr"),
    )
    EZRA = 15, "Ezra", r"(Ezr\.*(?:a)?|Esd\.*|Esdras|Ed\.*)", ("Ezr", "Esd", "Ed")
    NEHEMIAH = 16, "Nehemiah", r"(Neh\.*(?:emiah)?|Ne\.*|Neemias|Ne\.*)", ("Neh", "Ne")
    ESTHER = 17, "Esther", r"(Est\.*(?:h\.*)?(?:er)?|Est\.*|Ester|Et\.*)", ("Est", "Esth", "Et")
    JOB = 18, "Job", r"(Job|Jb\.*|Jó\.*)", ("Job", "Jb", "Jó")
    PSALMS = (
        19,
        "Psalms",
        r"(Psalms|Psalm|Pslm\.*|Psa\.*|Psm\.*|Pss\.*|Ps\.*|Salmos|Sal\.*|Sl\.*)",
        ("Ps", "Psa", "Pslm", "Psm", "Pss", "Sal", "Sl"),
    )
    PROVERBS = (
        20,
        "Proverbs",
        r"(Proverbs|Prov\.*|Pro\.*|Prv\.*|Proverbios|Prov\.*|Provérbios|Pv\.*)",
        ("Pro", "Prov", "Prv", "Pv"),
    )
    ECCLESIASTES = (
        21,
        "Ecclesiastes",
        r"(Ecclesiastes(?:\s+or\,\s+the\s+Preacher)?|Eclesiastés|Eclesiastes"
        r"|Eccles\.*(?!iasticus?)|Ecles\.*"
        r"|Eccle\.*(?!siasticus?)|Ecle\.*"
        r"|Eccl\.*(?!esiasticus?)(?!us?)|Ecl\.*"
        r"|Ecc\.*(?!lesiasticus?)(?!lus?)|Ec\.*|Ecl\.*|Qoh\.*)",
        ("Ec", "Ecc", "Eccl", "Eccle", "Eccles", "Ecl", "Ecle", "Ecles", "Qoh"),
    )
    SONG_OF_SONGS = (
        22,
        "Song of Songs",
        r"(Song(?: of (Solomon|Songs|Sol\.*))?|Cantar de los Cantares|Cânticos|Cantares|Ct\.*)"
        r"|Canticles|(Canticle(?: of Canticles)?)|SOS|Cant",
        ("Cant", "Canticle", "Canticles", "Song", "Song of Sol", "SOS", "Ct"),
    )
    ISAIAH = 23, "Isaiah", r"(Isa\.*(?:iah)?|Isaias|Isa\.*|Is\.*)", ("Isa", "Is")
    JEREMIAH = 24, "Jeremiah", r"(Jer\.*(?:emiah)?|Jeremias|Jer\.*|Je\.*|Jr\.*)", ("Jer", "Je", "Jr")
    LAMENTATIONS = (
        25,
        "Lamentations",
        _build_book_regular_expression(
            r"(Lam\.*(?:entations)?|Lamentaciones|Lamentações|Lam\.*|Lm\.*|Lá\.*)",
            suffix=r"of\s+Jeremiah",
        ),
        ("Lam", "Lm", "Lá"),
    )
    EZEKIEL = 26, "Ezekiel", r"(Ezekiel|Ezequiel|Eze\.*|Ezq\.*|Ezk\.*|Ez\.*)", ("Eze", "Ezq", "Ezk", "Ez")
    DANIEL = 27, "Daniel", r"(Dan\.*(?:iel)?|Dan\.*|Dn\.*)", ("Dan", "Dn")
    HOSEA = 28, "Hosea", r"(Hos\.*(?:ea)?|Oseas|Os\.*|O\.*)", ("Hos", "Os", "O")
    JOEL = 29, "Joel", r"(Joe\.*(?:l)?|Joel|Jl\.*)", ("Joe", "Jl")
    AMOS = 30, "Amos", r"(Amo\.*(?:s)?|Amós|Am\.*)", ("Amo", "Am")
    OBADIAH = 31, "Obadiah", r"(Oba\.*(?:d\.*(?:iah)?)?|Abdías|Obd\.*|Abd\.*|Ob\.*|Ab\.*)", ("Oba", "Obd", "Abd", "Ob", "Ab")
    JONAH = 32, "Jonah", r"(Jonah|Jon\.*|Jnh\.*|Jonás|Jn\.*|Jnh\.*)", ("Jnh", "Jon", "Jn")
    MICAH = 33, "Micah", r"(Mic\.*(?:ah)?|Miqueas|Mi\.*|Mq\.*)", ("Mic", "Mi", "Mq")
    NAHUM = 34, "Nahum", r"(?<!Jo)(Nah\.*(?:um)?|Nahúm|Na\.*)", ("Nah", "Na")
    HABAKKUK = 35, "Habakkuk", r"(Hab\.*(?:akkuk)?|Habacuc|Hab\.*|Hb\.*|Hc\.*)", ("Hab", "Hb", "Hc")
    ZEPHANIAH = 36, "Zephaniah", r"(Zep\.*(?:h\.*(?:aniah)?)?|Sofonías|Zefanias|Sof\.*|Zef\.*|Sf\.*|Zp\.*)", ("Zep", "Sof", "Zef", "Sf", "Zp")
    HAGGAI = 37, "Haggai", r"(Hag\.*(?:gai)?|Ageo|Ag\.*|Hg\.*)", ("Hag", "Ag", "Hg")
    ZECHARIAH = 38, "Zechariah", r"(Zec\.*(?:h\.*(?:ariah)?)?|Zacarías|Zacarias|Zac\.*|Zc\.*)", ("Zec", "Zac", "Zc")
    MALACHI = 39, "Malachi", r"(Mal\.*(?:achi)?|Malaquías|Malaquias|Mal\.*|Ml\.*)", ("Mal", "Ml")
    MATTHEW = 40, "Matthew", r"(Mat\.*(?:t\.*(?:hew)?)?|Mateo|Mat\.*|Mt\.*)", ("Mat", "Matt", "Mt")
    MARK = 41, "Mark", r"(Mark|Mar\.*|Mrk\.*|Marcos|Mr\.*|Mc\.*)", ("Mar", "Mrk", "Mr", "Mc")
    LUKE = 42, "Luke", r"(Luk\.*(?:e)?|Lucas|Luc\.*|Lc\.*)", ("Luk", "Luc", "Lc")
    JOHN = (
        43,
        "John",
        rf"(?<!(?:1|2|3|I)\s)(?<!(?:1|2|3|I)){_JOHN_REGULAR_EXPRESSION}",
        ("Jhn", "Jn", "Jo", "Joh"),
    )
    ACTS = (
        44,
        "Acts",
        _build_book_regular_expression(
            r"(Act\.*(?:s)?|Hechos|Atos|Act\.*|He\.*|At\.*)",
            suffix="of the Apostles",
        ),
        ("Act", "He", "At"),
    )
    ROMANS = 45, "Romans", r"(Rom\.*(?:ans)?|Romanos|Rom\.*|Rm\.*)", ("Rom", "Rm")
    CORINTHIANS_1 = (
        46,
        "1 Corinthians",
        _build_book_regular_expression(
            _CORINTHIANS_REGULAR_EXPRESSION,
            prefix=_FIRST_PAUL_EPISTLE,
        ),
        ("Co", "Cor", "1Co"),
    )
    CORINTHIANS_2 = (
        47,
        "2 Corinthians",
        _build_book_regular_expression(
            _CORINTHIANS_REGULAR_EXPRESSION,
            prefix=_SECOND_PAUL_EPISTLE,
        ),
        ("Co", "Cor", "2Co"),
    )
    GALATIANS = 48, "Galatians", r"(Gal\.*(?:atians)?|Gálatas|Gal\.*|Gl\.*)", ("Gal", "Gl")
    EPHESIANS = 49, "Ephesians", r"(?<!Z)(Eph\.*(?:es\.*(?:ians)?)?|Efesios|Efésios|Efe\.*|Ef\.*)", ("Eph", "Ephes", "Efe", "Ef")
    PHILIPPIANS = (
        50,
        "Philippians",
        r"(Ph(?:(p\.*)|(?:il\.*(?!e\.*(?:m\.*(?:on)?)?)(?:ippians)?))|Filipenses|Flp\.*|Fp\.*)",
        ("Php", "Phil", "Flp", "Fp"),
    )
    COLOSSIANS = 51, "Colossians", r"(Col\.*(?:ossians)?|Colosenses|Colossenses|Col\.*|Cl\.*)", ("Col", "Cl")
    THESSALONIANS_1 = (
        52,
        "1 Thessalonians",
        _build_book_regular_expression(
            _THESSALONIANS_REGULAR_EXPRESSION,
            prefix=_FIRST_PAUL_EPISTLE,
        ),
        ("Th", "Thes", "Thess", "Ths", "1Ts"),
    )
    THESSALONIANS_2 = (
        53,
        "2 Thessalonians",
        _build_book_regular_expression(
            _THESSALONIANS_REGULAR_EXPRESSION,
            prefix=_SECOND_PAUL_EPISTLE,
        ),
        ("Th", "Thes", "Thess", "Ths", "2Ts"),
    )
    TIMOTHY_1 = (
        54,
        "1 Timothy",
        _build_book_regular_expression(
            _TIMOTHY_REGULAR_EXPRESSION,
            prefix=_FIRST_PAUL_EPISTLE,
        ),
        ("Ti", "Tim", "1Tm"),
    )
    TIMOTHY_2 = (
        55,
        "2 Timothy",
        _build_book_regular_expression(
            _TIMOTHY_REGULAR_EXPRESSION,
            prefix=_SECOND_PAUL_EPISTLE,
        ),
        ("Ti", "Tim", "2Tm"),
    )
    TITUS = 56, "Titus", r"(Tit\.*(?:us)?|Tito|Tit\.*|Tt\.*)", ("Tit", "Tt")
    PHILEMON = (
        57,
        "Philemon",
        r"(Philemon|Philem\.*|Phile\.*|Phlm\.*|Phi\.*(?!l)|Phm\.*|Filemón|Filemon|Flm\.*|Fm\.*)",
        ("Phi", "Phile", "Philem", "Phlm", "Phm", "Flm", "Fm"),
    )
    HEBREWS = 58, "Hebrews", r"(Heb\.*(?:rews)?|Hebreos|Hebreus|Heb\.*|Hb\.*)", ("Heb", "Hb")
    JAMES = 59, "James", r"(Ja(?:me)?s\.*|Santiago|Tiago|San\.*|Stg\.*|Tg\.*)", ("Jas", "San", "Stg", "Tg")
    PETER_1 = (
        60,
        "1 Peter",
        _build_book_regular_expression(
            _PETER_REGULAR_EXPRESSION,
            prefix=_FIRST_GENERAL_EPISTLE,
        ),
        ("Pe", "Pet", "Pt", "1Pe"),
    )
    PETER_2 = (
        61,
        "2 Peter",
        _build_book_regular_expression(
            _PETER_REGULAR_EXPRESSION,
            prefix=_SECOND_GENERAL_EPISTLE,
        ),
        ("Pe", "Pet", "Pt", "2Pe"),
    )
    JOHN_1 = (
        62,
        "1 John",
        _build_book_regular_expression(
            _JOHN_REGULAR_EXPRESSION,
            prefix=_FIRST_GENERAL_EPISTLE,
        ),
        ("Jhn", "Jn", "Jo", "Joh", "1Jo"),
    )
    JOHN_2 = (
        63,
        "2 John",
        _build_book_regular_expression(
            _JOHN_REGULAR_EXPRESSION,
            prefix=_SECOND_GENERAL_EPISTLE,
        ),
        ("Jhn", "Jn", "Jo", "Joh", "2Jo"),
    )
    JOHN_3 = (
        64,
        "3 John",
        _build_book_regular_expression(
            _JOHN_REGULAR_EXPRESSION,
            prefix=_THIRD_GENERAL_EPISTLE,
        ),
        ("Jhn", "Jn", "Jo", "Joh", "3Jo"),
    )
    JUDE = 65, "Jude", r"(Jud\.*(:?e)?(?!ges)|Judas|Jd\.*)", ("Jud", "Jd")
    REVELATION = (
        66,
        "Revelation",
        _build_book_regular_expression(
            r"(Rev\.*(?:elation)?|Apocalipsis|Apocalipse|Rev\.*|Ap\.*)",
            suffix="of ((Jesus Christ)|John|(St. John the Divine))",
        ),
        ("Rev", "Ap"),
    )
    ESDRAS_1 = (
        67,
        "1 Esdras",
        _build_book_regular_expression(
            r"(Esdras|Esdr\.*|Esd\.*|Es\.*)",
            _FIRST,
        ),
        ("Es", "Esd", "Esdr"),
    )
    TOBIT = 68, "Tobit", r"(Tobit|Tob\.*|Tb\.*|Tobías|Tobias|Tb\.*)", ("Tb", "Tob")
    WISDOM_OF_SOLOMON = (
        69,
        "Wisdom of Solomon",
        r"(Wisdom of Solomon|Wisdom|Sabiduría|Sabedoria|Wisd\.* of Sol\.*|Wis\.*|(?<!Hebre)Ws\.*)",
        ("Wis", "Wisd of Sol", "Ws", "Sab", "Sb"),
    )
    ECCLESIASTICUS = (
        70,
        "Ecclesiasticus",
        r"(Sirach|Sir\.*|Eclesiástico|Eclesiástico|Ecclesiasticus|Ecclus\.*)",
        ("Ecclus", "Sir", "Eclo", "Ecl"),
    )
    MACCABEES_1 = (
        71,
        "1 Maccabees",
        _build_book_regular_expression(
            _MACCABEES_REGULAR_EXPRESSION,
            _FIRST,
        ),
        ("M", "Ma", "Mac", "Macc"),
    )
    MACCABEES_2 = (
        72,
        "2 Maccabees",
        _build_book_regular_expression(
            _MACCABEES_REGULAR_EXPRESSION,
            _SECOND,
        ),
        ("M", "Ma", "Mac", "Macc"),
    )
