from django.contrib.auth.models import BaseUserManager


class UsuarioManager(BaseUserManager):
    def create_user(self, nome, email, password):
        if not email:
            raise ValueError("Usuario precisa de um email")
        usuario = self.model(nome=nome, email=self.normalize_email(email))
        usuario.set_password(password)
        usuario.save()
        return usuario
