import gettext
import os.path
import re
from importlib import metadata as _importlib_metadata
from unittest.mock import patch

import pytest

import country
import country.db


@pytest.fixture
def countries():
    country.countries._clear()
    yield country.countries
    country.countries._clear()


def test_country_list(countries):
    assert len(country.countries) == 249
    assert isinstance(list(country.countries)[0], country.db.Data)


def test_country_fuzzy_search(countries):
    results = country.countries.search_fuzzy("England")
    assert len(results) == 1
    assert results[0] == country.countries.get(alpha_2="GB")

    # Match alternative names exactly and thus NL ends up with
    # "Sint Maarten" before SX with "Sint Maarten (Dutch part)"
    results = country.countries.search_fuzzy("Sint Maarten")
    assert len(results) == 2
    assert results[0] == country.countries.get(alpha_2="NL")
    assert results[1] == country.countries.get(alpha_2="SX")

    # Match with accents removed, first a country with a partial match in the
    # country name, then a country with multiple subdivision partial matches,
    # and then a country with a single subdivision match.
    results = country.countries.search_fuzzy("Cote")
    assert len(results) == 3
    assert results[0] == country.countries.get(alpha_2="CI")
    assert results[1] == country.countries.get(alpha_2="FR")
    assert results[2] == country.countries.get(alpha_2="HN")

    # A somewhat carefully balanced point system allows for a (bias-based)
    # graceful sorting of common substrings being used in multiple matches:
    results = country.countries.search_fuzzy("New")
    assert results[0] == country.countries.get(alpha_2="NC")
    assert results[1] == country.countries.get(alpha_2="NZ")
    assert results[2] == country.countries.get(alpha_2="PG")
    assert results[3] == country.countries.get(alpha_2="GB")
    assert results[4] == country.countries.get(alpha_2="US")
    assert results[5] == country.countries.get(alpha_2="CA")
    assert results[6] == country.countries.get(alpha_2="AU")
    assert results[7] == country.countries.get(alpha_2="BS")
    assert results[8] == country.countries.get(alpha_2="TW")
    assert results[9] == country.countries.get(alpha_2="MH")

    # bug #34, likely about capitalization that was broken
    results = country.countries.search_fuzzy("united states of america")
    assert len(results) == 1
    assert results[0] == country.countries.get(alpha_2="US")


def test_historic_country_fuzzy_search(countries):
    results = country.historic_countries.search_fuzzy("burma")
    assert len(results) == 1
    assert results[0] == country.historic_countries.get(alpha_4="BUMM")


def test_germany_has_all_attributes(countries):
    germany = country.countries.get(alpha_2="DE")
    assert germany.alpha_2 == "DE"
    assert germany.alpha_3 == "DEU"
    assert germany.numeric == "276"
    assert germany.name == "Germany"
    assert germany.official_name == "Federal Republic of Germany"


def test_missing_common_official(countries):
    aruba = country.countries.get(alpha_2="AW")
    assert aruba.alpha_2 == "AW"
    assert aruba.name == "Aruba"
    with pytest.raises(AttributeError, match="official_name"):
        aruba.official_name
    with pytest.raises(AttributeError, match="common_name"):
        aruba.common_name


def test_missing_common_official_use_different(countries):
    vietnam = country.countries.get(alpha_2="VN")
    assert vietnam.alpha_2 == "VN"
    assert vietnam.name == "Viet Nam"
    assert vietnam.official_name == "Socialist Republic of Viet Nam"
    assert vietnam.common_name == "Vietnam"


def test_country_missing_attribute(countries):
    germany = country.countries.get(alpha_2="DE")
    with pytest.raises(AttributeError):
        _ = germany.foo


def test_subdivisions_directly_accessible(countries):
    assert len(country.subdivisions) == 5046
    assert isinstance(list(country.subdivisions)[0], country.db.Data)

    de_st = country.subdivisions.get(code="DE-ST")
    assert de_st.code == "DE-ST"
    assert de_st.name == "Sachsen-Anhalt"
    assert de_st.type == "Land"
    assert de_st.parent is None
    assert de_st.parent_code is None
    assert de_st.country is country.countries.get(alpha_2="DE")


def test_subdivisions_have_subdivision_as_parent():
    fr_01 = country.subdivisions.get(code="FR-01")
    assert fr_01.code == "FR-01"
    assert fr_01.name == "Ain"
    assert fr_01.type == "Metropolitan department"
    assert fr_01.parent_code == "FR-ARA"
    assert fr_01.parent is country.subdivisions.get(code="FR-ARA")
    assert fr_01.parent.name == "Auvergne-Rhône-Alpes"


def test_query_subdivisions_of_country():
    assert len(country.subdivisions.get(country_code="DE")) == 16
    assert len(country.subdivisions.get(country_code="US")) == 57


def test_scripts():
    assert len(country.scripts) == 182
    assert isinstance(list(country.scripts)[0], country.db.Data)

    latin = country.scripts.get(name="Latin")
    assert latin.alpha_4 == "Latn"
    assert latin.name == "Latin"
    assert latin.numeric == "215"


def test_currencies():
    assert len(country.currencies) == 181
    assert isinstance(list(country.currencies)[0], country.db.Data)

    argentine_peso = country.currencies.get(alpha_3="ARS")
    assert argentine_peso.alpha_3 == "ARS"
    assert argentine_peso.name == "Argentine Peso"
    assert argentine_peso.numeric == "032"


def test_languages():
    assert len(country.languages) == 7910
    assert isinstance(list(country.languages)[0], country.db.Data)

    aragonese = country.languages.get(alpha_2="an")
    assert aragonese.alpha_2 == "an"
    assert aragonese.alpha_3 == "arg"
    assert aragonese.name == "Aragonese"

    bengali = country.languages.get(alpha_2="bn")
    assert bengali.name == "Bengali"
    assert bengali.common_name == "Bangla"

    # this tests the slow search path in lookup()
    bengali2 = country.languages.lookup("bAngLa")
    assert bengali2 == bengali


def test_language_families():
    assert len(country.language_families) == 115
    assert isinstance(list(country.language_families)[0], country.db.Data)

    aragonese = country.languages.get(alpha_3="arg")
    assert aragonese.alpha_3 == "arg"
    assert aragonese.name == "Aragonese"


def test_locales():
    german = gettext.translation(
        "iso3166-1", country.LOCALES_DIR, languages=["de"]
    )
    assert german.gettext("Germany") == "Deutschland"


def test_removed_countries():
    ussr = country.historic_countries.get(alpha_3="SUN")
    assert isinstance(ussr, country.db.Data)
    assert ussr.alpha_4 == "SUHH"
    assert ussr.alpha_3 == "SUN"
    assert ussr.name == "USSR, Union of Soviet Socialist Republics"
    assert ussr.withdrawal_date == "1992-08-30"


def test_repr(countries):
    assert re.match(
        "Country\\(alpha_2=u?'DE', "
        "alpha_3=u?'DEU', "
        "flag='..', "
        "name=u?'Germany', "
        "numeric=u?'276', "
        "official_name=u?'Federal Republic of Germany'\\)",
        repr(country.countries.get(alpha_2="DE")),
    )


def test_dict(countries):
    country = country.countries.get(alpha_2="DE")
    exp = {
        "alpha_2": "DE",
        "alpha_3": "DEU",
        "name": "Germany",
        "numeric": "276",
        "official_name": "Federal Republic of Germany",
        "flag": country.flag,
    }
    assert dict(country) == exp


def test_dir(countries):
    germany = country.countries.get(alpha_2="DE")
    for n in "alpha_2", "alpha_3", "name", "numeric", "official_name":
        assert n in dir(germany)


def test_get(countries):
    c = country.countries
    with pytest.raises(TypeError):
        c.get(alpha_2="DE", alpha_3="DEU")
    assert c.get(alpha_2="DE") == c.get(alpha_3="DEU")
    assert c.get(alpha_2="Foo") is None
    tracer = object()
    assert c.get(alpha_2="Foo", default=tracer) is tracer


def test_lookup(countries):
    c = country.countries
    g = c.get(alpha_2="DE")
    assert g == c.get(alpha_2="de")
    assert g == c.lookup("de")
    assert g == c.lookup("DEU")
    assert g == c.lookup("276")
    assert g == c.lookup("germany")
    assert g == c.lookup("Federal Republic of Germany")
    # try a generated field
    bqaq = country.historic_countries.get(alpha_4="BQAQ")
    assert bqaq == country.historic_countries.lookup("atb")
    german = country.languages.get(alpha_2="de")
    assert german == country.languages.lookup("De")
    euro = country.currencies.get(alpha_3="EUR")
    assert euro == country.currencies.lookup("euro")
    latin = country.scripts.get(name="Latin")
    assert latin == country.scripts.lookup("latn")
    fr_ara = country.subdivisions.get(code="FR-ARA")
    assert fr_ara == country.subdivisions.lookup("fr-ara")
    with pytest.raises(LookupError):
        country.countries.lookup("bogus country")
    with pytest.raises(LookupError):
        country.countries.lookup(12345)
    with pytest.raises(LookupError):
        country.countries.get(alpha_2=12345)


def test_subdivision_parent():
    s = country.subdivisions
    sd = s.get(code="CV-BV")
    assert sd.parent_code == "CV-B"
    assert sd.parent is s.get(code=sd.parent_code)


def test_subdivision_missing_code_raises_keyerror():
    s = country.subdivisions
    assert s.get(code="US-ZZ") is None


def test_subdivision_empty_list():
    s = country.subdivisions
    assert len(s.get(country_code="DE")) == 16
    assert len(s.get(country_code="JE")) == 0
    assert s.get(country_code="FOOBAR") is None


def test_has_version_attribute():
    try:
        _importlib_metadata.distribution("pycountry")
    except _importlib_metadata.PackageNotFoundError:
        pytest.skip("pycountry not installed correctly, you're on your own")
    assert country.__version__ != "n/a"
    assert len(country.__version__) >= 5
    assert "." in country.__version__


def test_is_instance_of_language():
    assert isinstance(country.languages, country.Languages)


def test_is_instance_of_country(countries):
    united_states = country.countries.get(alpha_2="US")
    class_name = united_states.__class__.__name__
    assert class_name == "Country"


def test_is_instance_of_subdivision():
    assert isinstance(country.subdivisions, country.Subdivisions)


def test_is_instance_of_script():
    assert isinstance(country.scripts, country.Scripts)


def test_is_instance_of_currency():
    assert isinstance(country.currencies, country.Currencies)


def test_add_entry(countries):
    assert country.countries.get(alpha_2="XK") is None

    country.countries.add_entry(
        alpha_2="XK", alpha_3="XXK", name="Kosovo", numeric="926"
    )

    country = country.countries.get(alpha_2="XK")
    assert isinstance(country, country.countries.data_class)


def test_remove_entry(countries):
    assert country.countries.get(alpha_2="DE") is not None

    country.countries.remove_entry(alpha_2="DE")

    assert country.countries.get(alpha_2="DE") is None


def test_remove_non_existent_entry():
    with pytest.raises(KeyError, match="not found"):
        country.countries.remove_entry(name="Not A Real Country")


def test_no_results_lookup_error(countries):
    try:
        import importlib_resources  # type: ignore
    except ModuleNotFoundError:
        from importlib import resources as importlib_resources

    def resource_filename(package_or_requirement, resource_name):
        return str(
            importlib_resources.files(package_or_requirement) / resource_name
        )

    DATABASE_DIR = resource_filename("pycountry", "databases")
    countries = country.ExistingCountries(
        os.path.join(DATABASE_DIR, "iso3166-1.json")
    )

    query = "nonexistent query"
    with pytest.raises(LookupError):
        countries.search_fuzzy(query)


def test_subdivision_fuzzy_search_match():
    results = country.subdivisions.search_fuzzy("Alabama")
    assert len(results) == 1
    assert results[0].name == "Alabama"


def test_subdivision_fuzzy_search_partial_match():
    results = country.subdivisions.search_fuzzy("Massachusett")
    assert len(results) == 1
    assert results[0].name == "Massachusetts"


def test_subdivision_match():
    results = country.subdivisions.match("Alabama")
    assert len(results) == 1
    assert results[0].name == "Alabama"


def test_subdivision_partial_match():
    results = country.subdivisions.partial_match("Massachusett")
    assert len(results) == 1
    assert results[0].name == "Massachusetts"


def test_non_country_attribute_error():
    english = country.languages.get(name="English")
    with pytest.raises(AttributeError):
        english.official_name


def test_country_attribute_error(countries):
    canada = country.countries.get(alpha_2="CA")
    with pytest.raises(AttributeError):
        canada.maple_syrup


def test_with_accents():
    assert country.remove_accents("Café") == "Cafe"
    assert country.remove_accents("résumé") == "resume"
    assert country.remove_accents("naïve") == "naive"
    assert country.remove_accents("São Paulo") == "Sao Paulo"


def test_without_accents():
    assert country.remove_accents("apple") == "apple"
    assert country.remove_accents("banana") == "banana"


def test_empty_string():
    assert country.remove_accents("") == ""


def test_special_characters():
    assert country.remove_accents("!@#$%^&*()") == "!@#$%^&*()"


def test_unicode_characters():
    assert country.remove_accents("你好") == "你好"  # Chinese characters
    assert (
        country.remove_accents("こんにちは") == "こんにちは"
    )  # Japanese characters


def test_subdivision_search_fuzzy_non_existent_subdivision():
    with pytest.raises(LookupError):
        country.subdivisions.search_fuzzy("Non Existent Subdivision")


def test_subdivision_partial_match_non():
    result = country.subdivisions.partial_match("Non Existent Subdivision")
    assert len(result) == 0


def test_subdivision_match_non():
    result = country.subdivisions.match("Non Existent Subdivision")
    assert len(result) == 0


def test_get_version_with_package_not_found():
    # Mock importlib.metadata.version to raise PackageNotFoundError
    with patch(
        "importlib.metadata.version",
        side_effect=_importlib_metadata.PackageNotFoundError,
    ):
        # Call get_version with a package name that doesn't exist
        result = country.get_version("non_existent_package")

        # Assert that the result is 'n/a'
        assert result == "n/a"


def test_all_subdivisions_have_name_attribute():
    subdivisions = country.subdivisions
    has_name_attr = [
        hasattr(subdivision, "name") for subdivision in subdivisions
    ]
    all_have_name_attr = all(has_name_attr)

    assert all_have_name_attr


def test_subdivisions_with_missing_parents():
    result = [
        (i.code, i.parent_code)
        for i in country.subdivisions
        if i.parent_code and not i.parent
    ]
    assert result == []
