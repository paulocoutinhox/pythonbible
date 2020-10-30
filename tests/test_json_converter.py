import json
import os

import pytest

import pythonbible as bible
from pythonbible.bible.json_converter import JSONConverter

TEST_DATA_FOLDER = os.path.dirname(os.path.realpath(__file__))


def test_json_converter(kjv_parser, short_verse_id_list, short_verse_data_json):
    # Given a parser, a data folder, a list of verse ids, and no existing json file.
    json_filename = os.path.join(
        TEST_DATA_FOLDER, f"{kjv_parser.version.value.lower()}.json"
    )
    remove_file_if_exists(json_filename)

    # When we use the json converter to generate the json file
    json_converter = JSONConverter(
        kjv_parser, data_folder=TEST_DATA_FOLDER, verse_ids=short_verse_id_list
    )
    json_converter.generate_json_file()

    # Then the json file exists.
    assert os.path.exists(json_filename)

    # And the data in the file correctly contains the verse data.
    with open(json_filename) as json_file:
        verse_data = json.load(json_file)

    assert verse_data == short_verse_data_json

    # Clean Up (remove the file)
    remove_file_if_exists(json_filename)


def test_json_converter_null_parser():
    # Given a null parser
    json_converter = JSONConverter(None)

    # When we attempt to generate the JSON file
    # Then an error is raised.
    with pytest.raises(bible.InvalidBibleParserError):
        json_converter.generate_json_file()


def test_json_converter_invalid_parser_type():
    # Given a parser instance that is not a valid type
    json_converter = JSONConverter("invalid parser")

    # When we attempt to generate the JSON file
    # Then an error is raised.
    with pytest.raises(bible.InvalidBibleParserError):
        json_converter.generate_json_file()


def remove_file_if_exists(filename):
    try:
        os.remove(filename)
    except OSError:
        pass
