import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []

AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []

DOC_DOCUMENT = []
DOCX_DOCUMENT = []
TXT_DOCUMENT = []
PDF_DOCUMENT = []
XLSX_DOCUMENT = []
PPTX_DOCUMENT = []

MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []

MY_OTHER = []

ZIP_ARCHIVES = []
GZ_ARCHIVES = []
TAR_ARCHIVES = []


REGISTER_EXTENSION = {
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,
    'DOC': DOC_DOCUMENT,
    'DOCX': DOCX_DOCUMENT,
    'TXT': TXT_DOCUMENT,
    'PDF': PDF_DOCUMENT,
    'XLSX': XLSX_DOCUMENT,
    'PPTX': PPTX_DOCUMENT,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'MP3': MP3_AUDIO,
    'ZIP': ZIP_ARCHIVES,
    'GZ': GZ_ARCHIVES,
    'TAR': TAR_ARCHIVES,
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(name: str) -> str:
    return Path(name).suffix[1:].upper()  # suffix[1:] -> .jpg -> jpg

def scan(folder: Path):
    for item in folder.iterdir():
        # ������ � ������
        if item.is_dir():  # ���������� �� ���� �����
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'MY_OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue

        # ������ � ������
        extension = get_extension(item.name)  # ������ ���������� �����
        full_name = folder / item.name  # ������ ������ ���� �� �����
        if not extension:
            MY_OTHER.append(full_name)
        else:
            try:
                REGISTER_EXTENSION[extension]
                EXTENSIONS.add(extension)
            except KeyError:
                UNKNOWN.add(extension)  # .mp4, .mov, .avi
                MY_OTHER.append(full_name)

if __name__ == '__main__':
    folder_process = sys.argv[1]
    scan(Path(folder_process))
    
    print(f'Images jpeg: {JPEG_IMAGES}')
    print(f'Images jpg: {JPG_IMAGES}')
    print(f'Images png: {PNG_IMAGES}')
    print(f'Images svg: {SVG_IMAGES}')
    
    print(f'Video avi: {AVI_VIDEO}')
    print(f'Video mp4: {MP4_VIDEO}')
    print(f'Video mov: {MOV_VIDEO}')
    print(f'Video mkv: {MKV_VIDEO}')
    
    print(f'Document doc: {DOC_DOCUMENT}')
    print(f'Document docx: {DOCX_DOCUMENT}')
    print(f'Document txt: {TXT_DOCUMENT}')
    print(f'Document pdf: {PDF_DOCUMENT}')
    print(f'Document xlsx: {XLSX_DOCUMENT}')
    print(f'Document pptx: {PPTX_DOCUMENT}')

    print(f'AUDIO mp3: {MP3_AUDIO}')
    print(f'AUDIO ogg: {OGG_AUDIO}')
    print(f'AUDIO wav: {WAV_AUDIO}')
    print(f'AUDIO amr: {AMR_AUDIO}')

    print(f'Archives zip: {ZIP_ARCHIVES}')
    print(f'Archives gz: {GZ_ARCHIVES}')
    print(f'Archives tar: {TAR_ARCHIVES}')


    print(f'EXTENSIONS: {EXTENSIONS}')
    print(f'UNKNOWN: {UNKNOWN}')

