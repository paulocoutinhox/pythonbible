from __future__ import annotations

from enum import Enum
from typing import Any, Type


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
_KINGS_REGULAR_EXPRESSION = r"(Kings|Kgs\.*|Kin\.*|Ki\.*|Reyes|Reis|Re\.*|R\.*)"
_CHRONICLES_REGULAR_EXPRESSION = r"(Chronicles|Chron\.*|Chro\.*|Chr\.*|Ch\.*|Crónicas|Crônicas|Cr\.*|1Cr|2Cr|I Cr|II Cr|1 Cr|2 Cr)"
_JOHN_REGULAR_EXPRESSION = r"(John|Joh\.*|Jhn\.*|Jo\.*(?!shua|b|nah|el)|Jn\.*|Juan|João|J\.*|Jão)"
_CORINTHIANS_REGULAR_EXPRESSION = r"Co\.*(?:r\.*(?:inthians)?)?|Corintios|Coríntios|1Co|2Co|I Co|II Co|1 Co|2 Co"
_THESSALONIANS_REGULAR_EXPRESSION = r"Th\.*(?:(s|(es(?:s)?))\.*(?:alonians)?)?|Tesalonicenses|Tessalonicenses|1Th|2Th|I Th|II Th|1 Th|2 Th"
_TIMOTHY_REGULAR_EXPRESSION = r"Ti\.*(?:m\.*(?:othy)?)?|Timoteo|Timóteo|1Ti|2Ti|I Ti|II Ti|1 Ti|2 Ti"
_PETER_REGULAR_EXPRESSION = r"(Pe\.*(?:t\.*(?:er)?)?|Pt\.*|Pedro|1Pe|2Pe|I Pe|II Pe|1 Pe|2 Pe)"
_MACCABEES_REGULAR_EXPRESSION = r"(Maccabees|Macc\.*|Mac\.*|Ma\.*|M\.*|Macabeos|Macabeus|1Ma|2Ma|I Ma|II Ma|1 Ma|2 Ma)"

_FIRST = r"1|I\s+|1st\s+|First\s+|Primera|Primer|Primeira|Primeiro"
_SECOND = r"2|II|2nd\s+|Second\s+|Segunda|Segundo"
_THIRD = r"3|III|3rd\s+|Third\s+|Tercera|Tercero|Terceira|Terceiro"

_FIRST_BOOK = rf"{_FIRST}|(First\s+Book\s+of(?:\s+the)?)|(Primer\s+Libro\s+de(?:\s+la)?)|(Primeiro\s+Livro\s+de(?:\s+o)?)"
_SECOND_BOOK = rf"{_SECOND}|(Second\s+Book\s+of(?:\s+the)?)|(Segundo\s+Libro\s+de(?:\s+la)?)|(Segundo\s+Livro\s+de(?:\s+o)?)"

_EPISTLE_OF_PAUL_TO = r"Epistle\s+of\s+Paul\s+(?:the\s+Apostle\s+)?to(?:\s+the)?|Epístola\s+de\s+Pablo\s+a(?:\s+la)?|Epístola\s+de\s+Paulo\s+a(?:\s+o)?"
_GENERAL_EPISTLE_OF = r"(?:General\s+)?Epistle\s+(?:General\s+)?of|Epístola\s+General\s+de|Epístola\s+Geral\s+de"

_FIRST_PAUL_EPISTLE = rf"{_FIRST}|(First\s+{_EPISTLE_OF_PAUL_TO})|(Primera\s+{_EPISTLE_OF_PAUL_TO})|(Primeira\s+{_EPISTLE_OF_PAUL_TO})"
_SECOND_PAUL_EPISTLE = rf"{_SECOND}|(Second\s+{_EPISTLE_OF_PAUL_TO})|(Segunda\s+{_EPISTLE_OF_PAUL_TO})|(Segunda\s+{_EPISTLE_OF_PAUL_TO})"

_FIRST_GENERAL_EPISTLE = rf"{_FIRST}|(First\s+{_GENERAL_EPISTLE_OF})|(Primera\s+{_GENERAL_EPISTLE_OF})|(Primeira\s+{_GENERAL_EPISTLE_OF})"
_SECOND_GENERAL_EPISTLE = rf"{_SECOND}|(Second\s+{_GENERAL_EPISTLE_OF})|(Segunda\s+{_GENERAL_EPISTLE_OF})|(Segunda\s+{_GENERAL_EPISTLE_OF})"
_THIRD_GENERAL_EPISTLE = rf"{_THIRD}|(Third\s+{_GENERAL_EPISTLE_OF})|(Tercera\s+{_GENERAL_EPISTLE_OF})|(Terceira\s+{_GENERAL_EPISTLE_OF})"


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

    GENESIS = 1, "Genesis", r"Gen\.*(?:esis)?|Génesis|Gênesis", ("Gen", "Gn")
    EXODUS = 2, "Exodus", r"Exo\.*(?:d\.*)?(?:us)?|Éxodo|Êxodo", ("Exo", "Exod", "Ex")
    LEVITICUS = 3, "Leviticus", r"Lev\.*(?:iticus)?|Levítico|Levítico", ("Lev", "Lv")
    NUMBERS = 4, "Numbers", r"Num\.*(?:bers)?|Números|Números", ("Num", "Nm")
    DEUTERONOMY = 5, "Deuteronomy", r"Deu\.*(?:t\.*)?(?:eronomy)?|Deuteronomio|Deuteronômio", ("Deu", "Deut", "Dt")
    JOSHUA = 6, "Joshua", r"(Joshua|Josh\.*|Jos\.*|Jsh\.*)|Josué|Josué", ("Jos", "Jsh", "Josh", "Js")
    JUDGES = 7, "Judges", r"(Judges|Judg\.*|Jdgs\.*|Jdg\.*)|Jueces|Juízes", ("Jdg", "Jdgs", "Judg", "Jz")
    RUTH = 8, "Ruth", r"(Ruth|Rut\.*|Rth\.*)|Rut|Rute", ("Rth", "Rut", "Rt")
    SAMUEL_1 = (
        9,
        "1 Samuel",
        _build_book_regular_expression(
            _SAMUEL_REGULAR_EXPRESSION,
            prefix=_FIRST_BOOK,
            suffix=r"Otherwise\s+Called\s+The\s+First\s+Book\s+of\s+the\s+Kings|Primer\s+Libro\s+de\s+Samuel|Primeiro\s+Livro\s+de\s+Samuel",
        ),
        ("Sa", "Sam", "Sm", "1 Sam", "1 S", "I Sam", "I S", "1Sa", "1S", "ISa", "IS"),
    )
    SAMUEL_2 = (
        10,
        "2 Samuel",
        _build_book_regular_expression(
            _SAMUEL_REGULAR_EXPRESSION,
            prefix=_SECOND_BOOK,
            suffix=r"Otherwise\s+Called\s+The\s+Second\s+Book\s+of\s+the\s+Kings|Segundo\s+Libro\s+de\s+Samuel|Segundo\s+Livro\s+de\s+Samuel",
        ),
        ("Sa", "Sam", "Sm", "2 Sam", "2 S", "II Sam", "II S", "2Sa", "2S", "IISa", "IIS"),
    )
    KINGS_1 = (
        11,
        "1 Kings",
        _build_book_regular_expression(
            _KINGS_REGULAR_EXPRESSION,
            prefix=_FIRST_BOOK,
            suffix=r"\,\s+Commonly\s+Called\s+the\s+Third\s+Book\s+of\s+the\s+Kings|Primer\s+Libro\s+de\s+Reyes|Primeiro\s+Livro\s+de\s+Reis",
        ),
        ("Kgs", "Ki", "Kin", "1 Kgs", "1 Ki", "1 Kin", "I Kgs", "I Ki", "I Kin", "1Re", "1R", "IRe", "IR"),
    )
    KINGS_2 = (
        12,
        "2 Kings",
        _build_book_regular_expression(
            _KINGS_REGULAR_EXPRESSION,
            prefix=_SECOND_BOOK,
            suffix=r"\,\s+Commonly\s+Called\s+the\s+Fourth\s+Book\s+of\s+the\s+Kings|Segundo\s+Libro\s+de\s+Reyes|Segundo\s+Livro\s+de\s+Reis",
        ),
        ("Kgs", "Ki", "Kin", "2 Kgs", "2 Ki", "2 Kin", "II Kgs", "II Ki", "II Kin", "2Re", "2R", "IIRe", "IIR"),
    )
    CHRONICLES_1 = (
        13,
        "1 Chronicles",
        _build_book_regular_expression(
            _CHRONICLES_REGULAR_EXPRESSION,
            prefix=_FIRST_BOOK,
        ),
        ("Ch", "Chr", "Chro", "Chron", "1 Chr", "1 Ch", "I Chr", "I Ch", "1Cr", "I Cr"),
    )
    CHRONICLES_2 = (
        14,
        "2 Chronicles",
        _build_book_regular_expression(
            _CHRONICLES_REGULAR_EXPRESSION,
            prefix=_SECOND_BOOK,
        ),
        ("Ch", "Chr", "Chro", "Chron", "2 Chr", "2 Ch", "II Chr", "II Ch", "2Cr", "II Cr"),
    )
    EZRA = 15, "Ezra", r"Ezr\.*(?:a)?|Esdras|Esdr", ("Ezr", "Esd", "Ed")
    NEHEMIAH = 16, "Nehemiah", r"Neh\.*(?:emiah)?|Nehemías|Neemias", ("Neh", "Ne")
    ESTHER = 17, "Esther", r"Est\.*(?:h\.*)?(?:er)?|Ester", ("Est", "Esth", "Et")
    JOB = 18, "Job", "Job|Jb|Jó", ("Job", "Jb", "Jó")
    PSALMS = (
        19,
        "Psalms",
        r"(Psalms|Psalm|Pslm\.*|Psa\.*|Psm\.*|Pss\.*|Ps\.*)|Salmos|Sal",
        ("Ps", "Psa", "Pslm", "Psm", "Pss", "Sal"),
    )
    PROVERBS = (
        20,
        "Proverbs",
        r"(Proverbs|Prov\.*|Pro\.*|Prv\.*)|Proverbios|Provérbios",
        ("Pro", "Prov", "Prv", "Pr"),
    )
    ECCLESIASTES = (
        21,
        "Ecclesiastes",
        r"(Ecclesiastes(?:\s+or\,\s+the\s+Preacher)?"
        r"|Eccles\.*(?!iasticus?)"
        r"|Eccle\.*(?!siasticus?)"
        r"|Eccl\.*(?!esiasticus?)(?!us?)"
        r"|Ecc\.*(?!lesiasticus?)(?!lus?)"
        r"|(?<!Z)Ec\.*(?!clesiasticus?)(?!clus?)|Qoh\.*)|Eclesiastés|Eclesiastes",
        ("Ec", "Ecc", "Eccl", "Eccle", "Eccles", "Qoh", "Ecl"),
    )
    SONG_OF_SONGS = (
        22,
        "Song of Songs",
        r"(Song(?: of (Solomon|Songs|Sol\.*))?)"
        "|Canticles|(Canticle(?: of Canticles)?)|SOS|Cant|Cantares|Cant",
        ("Cant", "Canticle", "Canticles", "Song", "Song of Sol", "SOS", "Ct"),
    )
    ISAIAH = 23, "Isaiah", r"Isa\.*(?:iah)?|Isaías", ("Isa", "Is")
    JEREMIAH = 24, "Jeremiah", r"Jer\.*(?:emiah)?|Jeremías|Jeremias", ("Jer", "Jr")
    LAMENTATIONS = (
        25,
        "Lamentations",
        _build_book_regular_expression(
            r"Lam\.*(?:entations)?",
            suffix=r"of\s+Jeremiah|de\s+Jeremías|de\s+Jeremias",
        ),
        ("Lam", "Lm"),
    )
    EZEKIEL = 26, "Ezekiel", r"(Ezekiel|Ezek\.*|Eze\.*|Ezk\.*)|Ezequiel", ("Eze", "Ezek", "Ezk", "Ez")
    DANIEL = 27, "Daniel", r"Dan\.*(?:iel)?|Daniel", ("Dan", "Dn")
    HOSEA = 28, "Hosea", r"Hos\.*(?:ea)?|Oseas|Oséias", ("Hos", "Os")
    JOEL = 29, "Joel", r"Joe\.*(?:l)?|Joel", ("Joe", "Jl")
    AMOS = 30, "Amos", r"Amo\.*(?:s)?|Amós", ("Amo", "Am")
    OBADIAH = 31, "Obadiah", r"Oba\.*(?:d\.*(?:iah)?)?|Abdías|Obadias", ("Oba", "Obad", "Abd")
    JONAH = 32, "Jonah", r"Jonah|Jon\.*|Jnh\.*|Jonás", ("Jnh", "Jon", "Jn")
    MICAH = 33, "Micah", r"Mic\.*(?:ah)?|Miqueas|Miquéias", ("Mic", "Mq")
    NAHUM = 34, "Nahum", r"(?<!Jo)Nah\.*(?:um)?|Nahúm", ("Nah", "Na")
    HABAKKUK = 35, "Habakkuk", r"Hab\.*(?:akkuk)?|Habacuc|Habacuque", ("Hab", "Hb")
    ZEPHANIAH = 36, "Zephaniah", r"Zep\.*(?:h\.*(?:aniah)?)?|Sofonías|Sofonias", ("Zep", "Zeph", "Sf")
    HAGGAI = 37, "Haggai", r"Hag\.*(?:gai)?|Hageo|Ageu", ("Hag", "Ag")
    ZECHARIAH = 38, "Zechariah", r"Zec\.*(?:h\.*(?:ariah)?)?|Zacarías|Zacarias", ("Zec", "Zech", "Zc")
    MALACHI = 39, "Malachi", r"Mal\.*(?:achi)?|Malaquías|Malaquias", ("Mal", "Ml")
    MATTHEW = 40, "Matthew", r"Mat\.*(?:t\.*(?:hew)?)?|Mateo|Mateus", ("Mat", "Matt", "Mt")
    MARK = 41, "Mark", r"Mark|Mar\.*|Mrk\.*|Marcos|Marcos", ("Mar", "Mrk", "Mc")
    LUKE = 42, "Luke", r"Luk\.*(?:e)?|Lucas", ("Luk", "Lc")
    JOHN = (
        43,
        "John",
        rf"(?<!(?:1|2|3|I)\s)(?<!(?:1|2|3|I)){_JOHN_REGULAR_EXPRESSION}|Juan|João",
        ("Jhn", "Jn", "Jo", "Joh", "J"),
    )
    ACTS = (
        44,
        "Acts",
        _build_book_regular_expression(
            r"Act\.*(?:s)?",
            suffix="of the Apostles|de los Apóstoles|dos Apóstolos",
        ),
        ("Act", "Hechos", "Atos", "Hch"),
    )
    ROMANS = 45, "Romans", r"Rom\.*(?:ans)?|Romanos", ("Rom", "Rm")
    CORINTHIANS_1 = (
        46,
        "1 Corinthians",
        _build_book_regular_expression(
            _CORINTHIANS_REGULAR_EXPRESSION,
            prefix=_FIRST_PAUL_EPISTLE,
        ),
        ("Co", "Cor", "1 Cor", "I Cor", "1Co", "ICo"),
    )
    CORINTHIANS_2 = (
        47,
        "2 Corinthians",
        _build_book_regular_expression(
            _CORINTHIANS_REGULAR_EXPRESSION,
            prefix=_SECOND_PAUL_EPISTLE,
        ),
        ("Co", "Cor", "2 Cor", "II Cor", "2Co", "IICo"),
    )
    GALATIANS = 48, "Galatians", r"Gal\.*(?:atians)?|Gálatas", ("Gal", "Gl")
    EPHESIANS = 49, "Ephesians", r"(?<!Z)Eph\.*(?:es\.*(?:ians)?)?|Efesios|Efésios", ("Eph", "Ef")
    PHILIPPIANS = (
        50,
        "Philippians",
        r"Ph(?:(p\.*)|(?:il\.*(?!e\.*(?:m\.*(?:on)?)?)(?:ippians)?))|Filipenses|Filipenses",
        ("Php", "Phil", "Fl"),
    )
    COLOSSIANS = 51, "Colossians", r"Col\.*(?:ossians)?|Colosenses|Colossenses", ("Col", "Cl")
    THESSALONIANS_1 = (
        52,
        "1 Thessalonians",
        _build_book_regular_expression(
            _THESSALONIANS_REGULAR_EXPRESSION,
            prefix=_FIRST_PAUL_EPISTLE,
        ),
        ("Th", "Thes", "Thess", "Ths", "1 Th", "1Th", "I Th", "ITh"),
    )
    THESSALONIANS_2 = (
        53,
        "2 Thessalonians",
        _build_book_regular_expression(
            _THESSALONIANS_REGULAR_EXPRESSION,
            prefix=_SECOND_PAUL_EPISTLE,
        ),
        ("Th", "Thes", "Thess", "Ths", "2 Th", "2Th", "II Th", "IITh"),
    )
    TIMOTHY_1 = (
        54,
        "1 Timothy",
        _build_book_regular_expression(
            _TIMOTHY_REGULAR_EXPRESSION,
            prefix=_FIRST_PAUL_EPISTLE,
        ),
        ("Ti", "Tim", "1 Ti", "1Ti", "I Ti", "ITi"),
    )
    TIMOTHY_2 = (
        55,
        "2 Timothy",
        _build_book_regular_expression(
            _TIMOTHY_REGULAR_EXPRESSION,
            prefix=_SECOND_PAUL_EPISTLE,
        ),
        ("Ti", "Tim", "2 Ti", "2Ti", "II Ti", "IITi"),
    )
    TITUS = 56, "Titus", r"Tit\.*(?:us)?|Tito", ("Tit", "Tt")
    PHILEMON = (
        57,
        "Philemon",
        r"(Philemon|Philem\.*|Phile\.*|Phlm\.*|Phi\.*(?!l)|Phm\.*)|Filemón|Filemom",
        ("Phi", "Phile", "Philem", "Phlm", "Phm", "Fl"),
    )
    HEBREWS = 58, "Hebrews", r"Heb\.*(?:rews)?|Hebreos|Hebreus", ("Heb", "Hb")
    JAMES = 59, "James", r"Ja(?:me)?s\.*|Santiago|Tiago", ("Jas", "Stg", "Tg")
    PETER_1 = (
        60,
        "1 Peter",
        _build_book_regular_expression(
            _PETER_REGULAR_EXPRESSION,
            prefix=_FIRST_GENERAL_EPISTLE,
        ),
        ("Pe", "Pet", "Pt", "1 Pe", "1Pe", "I Pe", "IPe"),
    )
    PETER_2 = (
        61,
        "2 Peter",
        _build_book_regular_expression(
            _PETER_REGULAR_EXPRESSION,
            prefix=_SECOND_GENERAL_EPISTLE,
        ),
        ("Pe", "Pet", "Pt", "2 Pe", "2Pe", "II Pe", "IIPe"),
    )
    JOHN_1 = (
        62,
        "1 John",
        _build_book_regular_expression(
            _JOHN_REGULAR_EXPRESSION,
            prefix=_FIRST_GENERAL_EPISTLE,
        ),
        ("Jhn", "Jn", "Jo", "Joh", "1 John", "1Jo", "I John", "IJo"),
    )
    JOHN_2 = (
        63,
        "2 John",
        _build_book_regular_expression(
            _JOHN_REGULAR_EXPRESSION,
            prefix=_SECOND_GENERAL_EPISTLE,
        ),
        ("Jhn", "Jn", "Jo", "Joh", "2 John", "2Jo", "II John", "IIJo"),
    )
    JOHN_3 = (
        64,
        "3 John",
        _build_book_regular_expression(
            _JOHN_REGULAR_EXPRESSION,
            prefix=_THIRD_GENERAL_EPISTLE,
        ),
        ("Jhn", "Jn", "Jo", "Joh", "3 John", "3Jo", "III John", "IIIJo"),
    )
    JUDE = 65, "Jude", r"Jud\.*(:?e)?(?!ges)|Judas", ("Jud", "Jd")
    REVELATION = (
        66,
        "Revelation",
        _build_book_regular_expression(
            r"Rev\.*(?:elation)?",
            suffix="of ((Jesus Christ)|John|(St. John the Divine))|Apocalipsis|Apocalipse",
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
        ("Es", "Esd", "Esdr", "1 Esd", "1Es", "I Esd", "IEs"),
    )
    TOBIT = 68, "Tobit", r"(Tobit|Tob\.*|Tb\.*|Tobías|Tobias)", ("Tb", "Tob")
    WISDOM_OF_SOLOMON = (
        69,
        "Wisdom of Solomon",
        r"(Wisdom of Solomon|Wisdom|Wisd\.* of Sol\.*|Wis\.*|(?<!Hebre)Ws\.*)|Sabiduría|Sabedoria",
        ("Wis", "Wisd of Sol", "Ws", "Sb"),
    )
    ECCLESIASTICUS = (
        70,
        "Ecclesiasticus",
        r"(Sirach|Sir\.*|Ecclesiasticus|Ecclus\.*)|Eclesiástico|Sirácida",
        ("Ecclus", "Sir", "Eclo"),
    )
    MACCABEES_1 = (
        71,
        "1 Maccabees",
        _build_book_regular_expression(
            _MACCABEES_REGULAR_EXPRESSION,
            _FIRST,
        ),
        ("M", "Ma", "Mac", "Macc", "1 Ma", "1Ma", "I Ma", "IMa"),
    )
    MACCABEES_2 = (
        72,
        "2 Maccabees",
        _build_book_regular_expression(
            _MACCABEES_REGULAR_EXPRESSION,
            _SECOND,
        ),
        ("M", "Ma", "Mac", "Macc", "2 Ma", "2Ma", "II Ma", "IIMa"),
    )
