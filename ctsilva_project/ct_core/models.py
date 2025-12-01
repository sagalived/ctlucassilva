from django.db import models
from django.core.validators import FileExtensionValidator
import os
import uuid 

# Função helper para garantir que o nome do arquivo seja único E que a extensão seja preservada.
def galeria_upload_path(instance, filename):
    """
    Gera um caminho de upload para a mídia da galeria com um nome de arquivo único (UUID), 
    preservando a extensão original. Isso corrige problemas de perda de extensão.
    """
    # 1. Pega a extensão original do arquivo
    name, ext = os.path.splitext(filename)
    
    # 2. Gera um nome de arquivo único usando UUID
    unique_filename = f'{uuid.uuid4()}{ext.lower()}' # Garante que a extensão seja minúscula
    
    # 3. Retorna o caminho completo: 'galeria/nome_unico.ext'
    return os.path.join('galeria', unique_filename)


class MediaGaleria(models.Model):
    titulo = models.CharField(max_length=100)
    
    # Data do evento para exibição (ex: "Treino de Domingo")
    data_evento = models.DateField(verbose_name="Data do Evento", help_text="Data em que a foto/vídeo foi feito.")
    
    # MÍDIA DE UPLOAD DIRETO: Campo FileField que aceita Imagem ou Arquivo de Vídeo
    # O upload_to agora usa a função customizada para preservar a extensão
    imagem = models.FileField(
        upload_to=galeria_upload_path, # CORREÇÃO APLICADA AQUI
        verbose_name='Foto ou Vídeo (Upload Direto)',
        null=True, 
        blank=True,
        help_text="Faça upload de uma imagem (JPG, PNG) ou um vídeo (MP4, MOV, WEBM).",
        # Validador para garantir extensões seguras de imagem e vídeo
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'mp4', 'mov', 'webm'])] 
    ) 

    # MÍDIA EXTERNA: Campo para links de vídeo EMBED (ex: iframe do YouTube)
    url_video = models.URLField(
        max_length=500, 
        null=True, 
        blank=True, 
        verbose_name='URL de Embed (YouTube/Vimeo)',
        help_text="Opcional: Use o link de EMBED (iframe) do YouTube ou outra plataforma. Preenchido, ignora o campo 'Foto ou Vídeo'."
    )

    data_upload = models.DateTimeField(auto_now_add=True)

    # PROPRIEDADE ESSENCIAL: Verifica se o arquivo em 'imagem' é um vídeo.
    @property
    def is_video_file(self):
        """Verifica a extensão do arquivo em 'imagem' para determinar se é um vídeo."""
        if self.imagem:
            # Pega a extensão do arquivo e converte para minúsculo
            ext = os.path.splitext(self.imagem.name)[1].lower()
            return ext in ['.mp4', '.mov', '.webm']
        return False
        
    def __str__(self):
        return f"{self.titulo} ({self.data_evento})"
    
    class Meta:
        verbose_name = "Item da Galeria (Foto/Vídeo)"
        verbose_name_plural = "Itens da Galeria"
        ordering = ['-data_evento', '-data_upload']