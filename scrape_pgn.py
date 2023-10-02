# Download monthly PGN archives for a given user, monthly

import urllib
import urllib.request
import argparse
import logging
import os
import subprocess

class parseChessComPGN:
    def __init__(self, args) -> None:
        self.username = args.username
        self.month = args.month
        self.year = args.year
        self.start_year = args.start_year
        self.start_month = args.start_month
        # eg: https://api.chess.com/pub/player/hikaru/games/2022/12/pgn
        self.download_path = args.download_path

    def get_monthly_pgn(self, year, month) -> None:
        baseUrl =  f"https://api.chess.com/pub/player/{self.username}/games/{year}/{month}/pgn"
        if not os.path.exists(self.download_path):
            os.makedirs(self.download_path)
        logging.info("Dowloading for " + year + "_" + month)
        subprocess.call(["curl", "-o", self.download_path + "/" + year + "_" + month +  ".pgn", baseUrl])


    def get_all_pgn(self):
        # All PGNs until the date provided
        for year in range(int(self.start_year), int(self.year)):
            for month in range(int(self.start_month), int(self.month)):
                month = str("%02d" % month)
                year = str(year)
                # '%02d' % month
                self.get_monthly_pgn(year, month)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", help="Input Username", type=str, default="dhingratul92")
    parser.add_argument("--download_path", help="download path", type=str, default="data/dhingratul92/pgn")
    parser.add_argument("--month", help="month", type=str, default="09")
    parser.add_argument("--year", help="year", type=str, default="2023")
    parser.add_argument("--start_year", help="start year", type=str, default="2015")
    parser.add_argument("--start_month", help="start month", type=str, default="03")
    args = parser.parse_args()
    chess_downloader = parseChessComPGN(args)
    # chess_downloader.get_monthly_pgn(args.year, args.month)
    chess_downloader.get_all_pgn()
