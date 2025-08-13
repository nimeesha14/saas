import healper
from typing import Any
from django.conf import settings
from django.core.management.base import BaseCommand

STATICFILES_VENDORS_DIR = getattr(settings, "STATICFILES_VENDORS_DIR")

VENDOR_STATICFILES = {
    "flowbite.min.css": "https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.css",
    "flowbite.min.js": "https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.js",
}
class Command(BaseCommand):


    def handle(self, *args:Any, **options:Any):
        self.stdout.write("Downloading vendor static files")
        compltete_urls = []
        for name, url in VENDOR_STATICFILES.items():

            out_path = STATICFILES_VENDORS_DIR / name
            dl_success = healper.download_to_local(url,out_path)
            if dl_success:
                compltete_urls.append(url)
            else:
                self.stdout.write(
                    self.style.ERROR(f"Failed to download {url}")
                )
        if set(compltete_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(self.style.SUCCESS('SUCCESSFULLY DOWNLOADED ALL VENDOR STATIC FILES'))
        else:
            self.stdout.write(self.style.ERROR('FAILED TO DOWNLOAD SOME VENDOR STATIC FILES'))







        
