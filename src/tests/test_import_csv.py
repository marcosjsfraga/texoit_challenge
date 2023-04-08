from services.csv_service import CSVService
from repositories.movies_repository import MoviesRepository

def test_import_data():
    csv_service = CSVService()
    movies_repository = MoviesRepository()

    result = csv_service.import_movielist()

    movies = movies_repository.get_movies()

    assert 'detail' in result
    assert 'rows_imported' in result
    assert result['detail'] == 'File already imported'
    assert result['rows_imported'] == len(movies)