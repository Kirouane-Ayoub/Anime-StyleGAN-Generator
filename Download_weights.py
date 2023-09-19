import gdown
def download_file_from_google_drive(file_id, output_file):
    """
    Download a file from Google Drive.

    :param file_id: The Google Drive file ID.
    :param output_file: The name of the file to save.
    """
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, output_file, quiet=False)

# Example usage:
file_id = "1-Iz1UHBRNlOQIZa44eEb0_2tTz85o9Ry"
file_out = "stylegan-step=4000.pt"
download_file_from_google_drive(file_id, file_out)