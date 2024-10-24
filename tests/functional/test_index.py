from src import create_app

def test_index_page():
    """
    DADO uma instância de teste da aplicação Flask
    QUANDO a página inicial é acessada via GET
    Então verifica se a resposta é válida
    """
    flask_app = create_app()  # Cria uma instância da aplicação

    # Cria um cliente de teste para a aplicação
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"Hello, World" in response.data
