from services.csv_service import CSVService

def test_import_data():
    csv_service = CSVService()

    result = csv_service.import_movielist()

    assert 'detail' in result
    assert 'rows_imported' in result
    
    print(f"-> COUNT: {result['rows_imported']}")

    assert result['detail'] == 'File already imported'
    # assert result['rows_imported'] == 3