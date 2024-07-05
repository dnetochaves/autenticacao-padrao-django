from ..models import Usuario


def cadastrar_usuario_service(usuario):
    Usuario.objects.create_user(
        nome=usuario.nome, email=usuario.email, password=usuario.password
    )
