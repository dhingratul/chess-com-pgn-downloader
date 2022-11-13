# Download monthly PGN archives for a given user, monthly

import urllib
import urllib.request
import argparse
import logging
import os


class parseChessComPGN:
    def __init__(self, username: str):
        self.username = username
        self.baseUrl = "https://api.chess.com/pub/player/" + self.username + "/games/"
        self.archivesUrl = self.baseUrl + "archives"

    def get_monthly_pgn(self, download_path: str) -> None:
        import pdb

        pdb.set_trace()
        if not os.path.exists(download_path):
            os.makedirs(download_path)
        f = urllib.request.urlopen(self.archivesUrl)
        archives = f.read().decode("utf-8")
        archives = archives.replace('{"archives":["', '","')
        archivesList = archives.split('","' + self.baseUrl)
        archivesList[len(archivesList) - 1] = archivesList[
            len(archivesList) - 1
        ].rstrip('"]}')

        for i in range(len(archivesList) - 1):
            url = self.baseUrl + archivesList[i + 1] + "/pgn"
            filename = archivesList[i + 1].replace("/", "-")
            urllib.request.urlretrieve(
                url, f"{download_path}/{self.username}" + filename + ".pgn"
            )
            logging.info(filename + ".pgn has been downloaded.")
        logging.info("All files have been downloaded.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", help="Input Username", type=str)
    parser.add_argument("--download_path", help="download path", type=str)
    args = parser.parse_args()
    chess_downloader = parseChessComPGN(args.username)
    chess_downloader.get_monthly_pgn(args.download_path)
