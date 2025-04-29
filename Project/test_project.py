from unittest.mock import patch, mock_open, Mock
from datetime import datetime, timedelta, timezone
import json
import requests
import project

sample_launches = [
    {
        "name": "Mission Alpha",
        "net": "2025-05-01T12:00:00Z",
        "launch_service_provider": {"name": "SpaceX"},
        "pad": {"location": {"country_code": "USA"}},
    },
    {
        "name": "Mission Beta",
        "net": "2025-06-15T14:30:00Z",
        "launch_service_provider": {"name": "NASA"},
        "pad": {"location": {"country_code": "USA"}},
    },
]


@patch("project.requests.get")
def test_fetch_launches_success(mock_get):
    mock_get.return_value = Mock(
        raise_for_status=Mock(), json=Mock(return_value={"results": sample_launches})
    )
    launches = project.fetch_launches()
    assert launches == sample_launches


@patch("project.requests.get", side_effect=requests.RequestException("API Error"))
def test_fetch_launches_failure(mock_get):
    launches = project.fetch_launches()
    assert launches == []


@patch("builtins.open", new_callable=mock_open)
def test_save_launches_offline(mock_file):
    project.save_launches_offline(sample_launches, "test_launches.json")
    mock_file.assert_called_with("test_launches.json", "w")


@patch("builtins.open", new_callable=mock_open, read_data=json.dumps(sample_launches))
def test_load_launches_offline(mock_file):
    launches = project.load_launches_offline("test_launches.json")
    assert launches == sample_launches


@patch("builtins.input", return_value="SpaceX")
@patch("builtins.print")
def test_filter_launches_by_agency(mock_print, mock_input):
    project.filter_launches_by_agency(sample_launches)
    assert mock_print.called


@patch("builtins.input", return_value="2025-05-01")
@patch("builtins.print")
def test_search_launches_by_date(mock_print, mock_input):
    project.search_launches_by_date(sample_launches)
    assert mock_print.called


@patch("builtins.print")
def test_countdown_to_next_launch(mock_print):
    future_time = (datetime.now(timezone.utc) + timedelta(days=1)).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )

    launches = [
        {
            "name": "Future Launch",
            "net": future_time,
            "launch_service_provider": {"name": "SpaceX"},
        }
    ]

    project.countdown_to_next_launch(launches)
    assert mock_print.called


@patch("builtins.input", return_value="1")
@patch("builtins.print")
def test_sort_launches_by_date(mock_print, mock_input):
    project.sort_launches_by_date(sample_launches)
    assert mock_print.called


@patch("builtins.input", return_value="NASA")
@patch("builtins.print")
def test_add_favorite_agency(mock_print, mock_input):
    project.favorite_agencies.clear()
    project.add_favorite_agency()
    assert "nasa" in project.favorite_agencies


@patch("builtins.print")
def test_show_launches_from_favorites(mock_print):
    project.favorite_agencies.clear()
    project.favorite_agencies.append("spacex")
    project.show_launches_from_favorites(sample_launches)
    assert mock_print.called


@patch("builtins.input", return_value="USA")
@patch("builtins.print")
def test_filter_launches_by_country(mock_print, mock_input):
    project.filter_launches_by_country(sample_launches)
    assert mock_print.called


@patch("builtins.print")
def test_random_launch_of_the_day(mock_print):
    project.random_launch_of_the_day(sample_launches)
    assert mock_print.called
