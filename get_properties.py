#!/usr/bin/env python
from oauth import authorize_creds, execute_request


def get_property_list(webmasters_service):
    '''
    Get a list of validated properties from GSC
    '''
    site_list = webmasters_service.sites().list().execute()

    # Filter for verified websites
    verified_sites_urls = [s['siteUrl'] for s in site_list['siteEntry']
                           if s['permissionLevel'] != 'siteUnverifiedUser'
                           and s['siteUrl'][:4] == 'http']
    return verified_sites_urls


if __name__ == '__main__':
    creds = './assets/client_secret.json'
    webmasters_service = authorize_creds(creds)
    verified_sites_urls = get_property_list(webmasters_service)