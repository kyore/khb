from datetime import date, timedelta


class Date:
    def __init__(self):
        self.today = date.today()
        self.download_start_date = self.today - timedelta(days=1)
        self.download_end_date = self.today - timedelta(days=1)

        if self.today.weekday() == 0:
            self.download_start_date = self.today - timedelta(days=3)
            self.download_end_date = self.today - timedelta(days=1)
