import requests
import json

def get_data():

	cookies = {
	    'COMPARISON_INDICATOR': 'false',
	    'HINTS_FIO_COOKIE_NAME': '1',
	    'MVID_2_exp_in_1': '1',
	    'MVID_AB_SERVICES_DESCRIPTION': 'var2',
	    'MVID_ADDRESS_COMMENT_AB_TEST': '2',
	    'MVID_BLACK_FRIDAY_ENABLED': 'true',
	    'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
	    'MVID_CART_MULTI_DELETE': 'true',
	    'MVID_CATALOG_STATE': '1',
	    'MVID_CITY_ID': 'CityR_32',
	    'MVID_FILTER_CODES': 'true',
	    'MVID_FILTER_TOOLTIP': '1',
	    'MVID_FLOCKTORY_ON': 'true',
	    'MVID_GEOLOCATION_NEEDED': 'true',
	    'MVID_GET_LOCATION_BY_DADATA': 'DaData',
	    'MVID_GIFT_KIT': 'true',
	    'MVID_IS_NEW_BR_WIDGET': 'true',
	    'MVID_KLADR_ID': '1600800100000',
	    'MVID_LAYOUT_TYPE': '1',
	    'MVID_LP_SOLD_VARIANTS': '0',
	    'MVID_NEW_ACCESSORY': 'true',
	    'MVID_NEW_DESKTOP_FILTERS': 'true',
	    'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
	    'MVID_NEW_LK_OTP_TIMER': 'true',
	    'MVID_NEW_MBONUS_BLOCK': 'true',
	    'MVID_REGION_ID': '26',
	    'MVID_REGION_SHOP': 'S951',
	    'MVID_SERVICES': '111',
	    'MVID_SERVICES_MINI_BLOCK': 'var2',
	    'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
	    'MVID_TIMEZONE_OFFSET': '3',
	    'MVID_WEBP_ENABLED': 'true',
	    'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
	    'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
	    'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
	    'searchType2': '2',
	    'admitad_deduplication_cookie': 'yandex.ru__organic',
	    '__SourceTracker': 'yandex.ru__organic',
	    'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
	    'afUserId': '871df56e-f396-46b8-9cca-8adfc86f3745-p',
	    '__ttl__widget__ui': '1656005438901-64576fa01fff',
	    'MVID_MCLICK': 'true',
	    'MVID_MOBILE_FILTERS': 'true',
	    '_ym_d': '1656933977',
	    '_ym_uid': '1656933977755583946',
	    'tmr_lvidTS': '1656933979310',
	    'tmr_lvid': 'ae43dfd8a08edeec113368b3f03bf4d4',
	    'uxs_uid': '20274340-fb8c-11ec-9137-f784351eff52',
	    'flocktory-uuid': '1039d19d-e43a-40cf-921d-be677a6f86b4-1',
	    'MVID_CRM_ID': '0043975070',
	    'wurfl_device_id': 'generic_web_browser',
	    'deviceType': 'desktop',
	    'MVID_GUEST_ID': '20996139372',
	    'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjpmYWxzZSwiZmF2b3JpdGUiOmZhbHNlLCJjYXJ0Ijp0cnVlfQ==',
	    'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOmZhbHNlLCJjb21wYXJpc29uIjpmYWxzZX0=',
	    '__lhash_': '215e3d8a4cdd6384b4ae977526536c98',
	    'MVID_CART_AVAILABILITY': '1',
	    'MVID_CREDIT_AVAILABILITY': 'true',
	    'MVID_GTM_DELAY': 'true',
	    'MVID_NEW_LK': 'true',
	    'MVID_NEW_LK_LOGIN': 'true',
	    'MVID_SMART_BANNER_BOTTOM': 'true',
	    'MVID_SUPER_FILTERS': 'false',
	    'flacktory': 'no',
	    '_gid': 'GA1.2.684216100.1658338280',
	    '_ym_isad': '1',
	    'authError': '',
	    'SMSError': '',
	    'advcake_track_id': '79b94a48-7d80-2d0c-62f6-afe4c0563816',
	    'advcake_session_id': '891cc368-6956-4265-7c60-34dd090351c6',
	    'JSESSIONID': 'byhTvYQVTJyNgHbV1gzpnVB8TjcTH0lj9DPqQNpJtZPqLrLvZsv8!1632987780',
	    'BIGipServeratg-ps-prod_tcp80': '2433014794.20480.0000',
	    'bIPs': '53593859',
	    'MVID_GTM_BROWSER_THEME': '1',
	    '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VbDCVBLXB6RWdvHh9cMUMlbFohR0kJT0kZNVxffR0jCWIzYx5uH2UzVSkTZGtJJylnDDt7GjxrIGFQYSZKXU1qJh8Wf24mWAsMXkFIb2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeDE+aCZjSF4iR1VJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MDkzJCpFWnw2fXZ9NGt5PwtwC1cwL2gMcRVNPUFxdjJCah1mR0sbNR0KQ2hSVENdLRtJUBg5Mzk0ZnBXJ2BNXiVMWVJ7Jh4aeHQfQU5EJ3VUNDpkdCIPaRMjZHhRP0VuWUZpdRUXQzwcew0qQ20tOmo=u1vTYw==',
	    '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VbDCVBLXB6RWdvHh9cMUMlbFohR0kJT0kZNVxffR0jCWIzYx5uH2UzVSkTZGtJJylnDDt7GjxrIGFQYSZKXU1qJh8Wf24mWAsMXkFIb2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeDE+aCZjSF4iR1VJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MDkzJCpFWnw2fXZ9NGt5PwtwC1cwL2gMcRVNPUFxdjJCah1mR0sbNR0KQ2hSVENdLRtJUBg5Mzk0ZnBXJ2BNXiVMWVJ7Jh4aeHQfQU5EJ3VUNDpkdCIPaRMjZHhRP0VuWUZpdRUXQzwcew0qQ20tOmo=u1vTYw==',
	    'cfidsgib-w-mvideo': 'VvSpOXB0JUmEdY8nolII67orgdqNAvYhZg6EH1+2bD2kuvr+Dbms/47ON495w/fij+MUAFxodjQEHZVBJFugpN3pzmR51+p2RCMvWPVxSRjvkp+KOEl00dnoVGZC1lSK7rliZkYhxvlQ8cNkdtW+2yCbMvR3IqCE3wvb3Dg=',
	    'cfidsgib-w-mvideo': 'VvSpOXB0JUmEdY8nolII67orgdqNAvYhZg6EH1+2bD2kuvr+Dbms/47ON495w/fij+MUAFxodjQEHZVBJFugpN3pzmR51+p2RCMvWPVxSRjvkp+KOEl00dnoVGZC1lSK7rliZkYhxvlQ8cNkdtW+2yCbMvR3IqCE3wvb3Dg=',
	    'gsscgib-w-mvideo': 'F3nDjVMF+hPFzx3XwgHAkar7RiNwdhKcWvF9Ul/jC881sp7UfSV2BAnB3lH5iNRdLpb5FUbFzv3HY4yeR5UUJQ0pMWjrO5QZwA5dkuJviqQSgpJVBHDSbENpDRTtPvxTE70i+nhew02clPPnVim/psiVG3U6621+o9SPRwvmzo4/I5Kpeq+Cj4jE+sm3x8LfwsXLIqbP/BWkUbpTbRS5s7qH3XvUrLZABmuhEZwJi5YC6aeIxY6q47267QO9t2vT',
	    'gsscgib-w-mvideo': 'F3nDjVMF+hPFzx3XwgHAkar7RiNwdhKcWvF9Ul/jC881sp7UfSV2BAnB3lH5iNRdLpb5FUbFzv3HY4yeR5UUJQ0pMWjrO5QZwA5dkuJviqQSgpJVBHDSbENpDRTtPvxTE70i+nhew02clPPnVim/psiVG3U6621+o9SPRwvmzo4/I5Kpeq+Cj4jE+sm3x8LfwsXLIqbP/BWkUbpTbRS5s7qH3XvUrLZABmuhEZwJi5YC6aeIxY6q47267QO9t2vT',
	    'fgsscgib-w-mvideo': 'MGmz2605cb0582b3340fa6a3ae2b5efbbd35805d',
	    'fgsscgib-w-mvideo': 'MGmz2605cb0582b3340fa6a3ae2b5efbbd35805d',
	    'cfidsgib-w-mvideo': 'T+51MiVQUGjAF0WNitdhfvwRMliBIGCr5h4STO5tvkkkEDO7SOBOapL1k6EW4RJc+PqPsoKrgO1mW3Qzz8xoKtVGQ7RupJgqKbpEhO/n71ipjIgpRT0pJIQsiCtiFPvRAR4fwXwccml/m8k4e0HUc11w44rGX15xy3YPYAg=',
	    'CACHE_INDICATOR': 'false',
	    'mindboxDeviceUUID': 'f28ead96-cc32-481e-85c4-ab7c73679772',
	    'directCrm-session': '%7B%22deviceGuid%22%3A%22f28ead96-cc32-481e-85c4-ab7c73679772%22%7D',
	    '_ga': 'GA1.2.391399013.1656005437',
	    'tmr_detect': '0%7C1658339429160',
	    'tmr_reqNum': '124',
	    '_ga_CFMZTSS5FM': 'GS1.1.1658338280.6.1.1658339545.0',
	    '_ga_BNX5WPP3YK': 'GS1.1.1658338280.6.1.1658339546.60',
	    'MVID_ENVCLOUD': 'prod2',
	}

	headers = {
	    'authority': 'www.mvideo.ru',
	    'accept': 'application/json',
	    'accept-language': 'ru,en;q=0.9,la;q=0.8',
	    # Requests sorts cookies= alphabetically
	    # 'cookie': 'COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=1; MVID_2_exp_in_1=1; MVID_AB_SERVICES_DESCRIPTION=var2; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=true; MVID_CART_MULTI_DELETE=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityR_32; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=1600800100000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=0; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_REGION_ID=26; MVID_REGION_SHOP=S951; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; searchType2=2; admitad_deduplication_cookie=yandex.ru__organic; __SourceTracker=yandex.ru__organic; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; afUserId=871df56e-f396-46b8-9cca-8adfc86f3745-p; __ttl__widget__ui=1656005438901-64576fa01fff; MVID_MCLICK=true; MVID_MOBILE_FILTERS=true; _ym_d=1656933977; _ym_uid=1656933977755583946; tmr_lvidTS=1656933979310; tmr_lvid=ae43dfd8a08edeec113368b3f03bf4d4; uxs_uid=20274340-fb8c-11ec-9137-f784351eff52; flocktory-uuid=1039d19d-e43a-40cf-921d-be677a6f86b4-1; MVID_CRM_ID=0043975070; wurfl_device_id=generic_web_browser; deviceType=desktop; MVID_GUEST_ID=20996139372; MVID_OLD_NEW=eyJjb21wYXJpc29uIjpmYWxzZSwiZmF2b3JpdGUiOmZhbHNlLCJjYXJ0Ijp0cnVlfQ==; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOmZhbHNlLCJjb21wYXJpc29uIjpmYWxzZX0=; __lhash_=215e3d8a4cdd6384b4ae977526536c98; MVID_CART_AVAILABILITY=1; MVID_CREDIT_AVAILABILITY=true; MVID_GTM_DELAY=true; MVID_NEW_LK=true; MVID_NEW_LK_LOGIN=true; MVID_SMART_BANNER_BOTTOM=true; MVID_SUPER_FILTERS=false; flacktory=no; _gid=GA1.2.684216100.1658338280; _ym_isad=1; authError=; SMSError=; advcake_track_id=79b94a48-7d80-2d0c-62f6-afe4c0563816; advcake_session_id=891cc368-6956-4265-7c60-34dd090351c6; JSESSIONID=byhTvYQVTJyNgHbV1gzpnVB8TjcTH0lj9DPqQNpJtZPqLrLvZsv8!1632987780; BIGipServeratg-ps-prod_tcp80=2433014794.20480.0000; bIPs=53593859; MVID_GTM_BROWSER_THEME=1; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VbDCVBLXB6RWdvHh9cMUMlbFohR0kJT0kZNVxffR0jCWIzYx5uH2UzVSkTZGtJJylnDDt7GjxrIGFQYSZKXU1qJh8Wf24mWAsMXkFIb2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeDE+aCZjSF4iR1VJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MDkzJCpFWnw2fXZ9NGt5PwtwC1cwL2gMcRVNPUFxdjJCah1mR0sbNR0KQ2hSVENdLRtJUBg5Mzk0ZnBXJ2BNXiVMWVJ7Jh4aeHQfQU5EJ3VUNDpkdCIPaRMjZHhRP0VuWUZpdRUXQzwcew0qQ20tOmo=u1vTYw==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VbDCVBLXB6RWdvHh9cMUMlbFohR0kJT0kZNVxffR0jCWIzYx5uH2UzVSkTZGtJJylnDDt7GjxrIGFQYSZKXU1qJh8Wf24mWAsMXkFIb2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeDE+aCZjSF4iR1VJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MDkzJCpFWnw2fXZ9NGt5PwtwC1cwL2gMcRVNPUFxdjJCah1mR0sbNR0KQ2hSVENdLRtJUBg5Mzk0ZnBXJ2BNXiVMWVJ7Jh4aeHQfQU5EJ3VUNDpkdCIPaRMjZHhRP0VuWUZpdRUXQzwcew0qQ20tOmo=u1vTYw==; cfidsgib-w-mvideo=VvSpOXB0JUmEdY8nolII67orgdqNAvYhZg6EH1+2bD2kuvr+Dbms/47ON495w/fij+MUAFxodjQEHZVBJFugpN3pzmR51+p2RCMvWPVxSRjvkp+KOEl00dnoVGZC1lSK7rliZkYhxvlQ8cNkdtW+2yCbMvR3IqCE3wvb3Dg=; cfidsgib-w-mvideo=VvSpOXB0JUmEdY8nolII67orgdqNAvYhZg6EH1+2bD2kuvr+Dbms/47ON495w/fij+MUAFxodjQEHZVBJFugpN3pzmR51+p2RCMvWPVxSRjvkp+KOEl00dnoVGZC1lSK7rliZkYhxvlQ8cNkdtW+2yCbMvR3IqCE3wvb3Dg=; gsscgib-w-mvideo=F3nDjVMF+hPFzx3XwgHAkar7RiNwdhKcWvF9Ul/jC881sp7UfSV2BAnB3lH5iNRdLpb5FUbFzv3HY4yeR5UUJQ0pMWjrO5QZwA5dkuJviqQSgpJVBHDSbENpDRTtPvxTE70i+nhew02clPPnVim/psiVG3U6621+o9SPRwvmzo4/I5Kpeq+Cj4jE+sm3x8LfwsXLIqbP/BWkUbpTbRS5s7qH3XvUrLZABmuhEZwJi5YC6aeIxY6q47267QO9t2vT; gsscgib-w-mvideo=F3nDjVMF+hPFzx3XwgHAkar7RiNwdhKcWvF9Ul/jC881sp7UfSV2BAnB3lH5iNRdLpb5FUbFzv3HY4yeR5UUJQ0pMWjrO5QZwA5dkuJviqQSgpJVBHDSbENpDRTtPvxTE70i+nhew02clPPnVim/psiVG3U6621+o9SPRwvmzo4/I5Kpeq+Cj4jE+sm3x8LfwsXLIqbP/BWkUbpTbRS5s7qH3XvUrLZABmuhEZwJi5YC6aeIxY6q47267QO9t2vT; fgsscgib-w-mvideo=MGmz2605cb0582b3340fa6a3ae2b5efbbd35805d; fgsscgib-w-mvideo=MGmz2605cb0582b3340fa6a3ae2b5efbbd35805d; cfidsgib-w-mvideo=T+51MiVQUGjAF0WNitdhfvwRMliBIGCr5h4STO5tvkkkEDO7SOBOapL1k6EW4RJc+PqPsoKrgO1mW3Qzz8xoKtVGQ7RupJgqKbpEhO/n71ipjIgpRT0pJIQsiCtiFPvRAR4fwXwccml/m8k4e0HUc11w44rGX15xy3YPYAg=; CACHE_INDICATOR=false; mindboxDeviceUUID=f28ead96-cc32-481e-85c4-ab7c73679772; directCrm-session=%7B%22deviceGuid%22%3A%22f28ead96-cc32-481e-85c4-ab7c73679772%22%7D; _ga=GA1.2.391399013.1656005437; tmr_detect=0%7C1658339429160; tmr_reqNum=124; _ga_CFMZTSS5FM=GS1.1.1658338280.6.1.1658339545.0; _ga_BNX5WPP3YK=GS1.1.1658338280.6.1.1658339546.60; MVID_ENVCLOUD=prod2',
	    'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118/f/skidka=da/tolko-v-nalichii=da',
	    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Yandex";v="22"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.134 Mobile Safari/537.36',
	    'x-set-application-id': 'ea45c09a-880c-4b8e-a822-836dabb8988e',
	}

	params = {
	    'categoryId': '118',
	    'offset': '0',
	    'limit': '24',
	    'filterParams': [
	        'WyJza2lka2EiLCIiLCJkYSJd',
	        'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
	    ],
	    'doTranslit': 'true',
	}

	response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()

	products_ids = response.get('body').get('products')
	with open('1_products_ids.json', 'w') as file:
		json.dump(products_ids, file, indent=4, ensure_ascii=False)
	
	json_data = {
    'productIds': products_ids,
    'mediaTypes': [
        'images',
    ],
    'category': True,
    'status': True,
    'brand': True,
    'propertyTypes': [
        'KEY',
    ],
    'propertiesConfig': {
        'propertiesPortionSize': 5,
    },
    'multioffer': False,
}

	response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=json_data).json()

	with open('2_items.json', 'w', encoding="utf-8") as file:
		json.dump(response, file, indent=4, ensure_ascii=False )

	products_ids_str= ','.join(products_ids)

	params = {
    'productIds': products_ids_str,
    'addBonusRubles': 'true',
    'isPromoApplied': 'true',
	}

	response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()

	with open('3_price.json', 'w', encoding="utf-8") as file:
		json.dump(response, file, indent=4, ensure_ascii=False)

	items_prices = {}

	material_prices = response.get('body').get('materialPrices')

	for item in material_prices:
		item_id = item.get('price').get('productId')
		item_base_price = item.get('price').get('basePrice')
		item_sale_price = item.get('price').get('salePrice')
		item_bonus = item.get('bonusRubles').get('total')

		items_prices[item_id] = {
			'item_basePrice': item_base_price,
			'item_salePrice': item_sale_price,
			'item_bonus': item_bonus
		}

	with open('4_items_prices.json', 'w', encoding="utf-8") as file:
		json.dump(items_prices, file, indent=4, ensure_ascii=False)

def get_result():
	with open('2_items.json', encoding="utf-8") as file:
		products_data = json.load(file)

	with open('4_items_prices.json', encoding="utf-8") as file:
		products_prices = json.load(file)

	products_data = products_data.get('body').get('products')

	for item in products_data:
		product_id = item.get('productId')

		if product_id in products_prices:
			prices = products_prices[product_id]

		item['item_basePrice'] = prices.get('item_basePrice')
		item['item_salePrice'] = prices.get('item_salePrice')
		item['item_bonus'] = prices.get('item_bonus')

	with open('5_result.json', 'w', encoding="utf-8") as file:
		json.dump(products_data, file, indent=4, ensure_ascii=False)

def main():
	get_data()
	get_result()

if __name__ == '__main__':
	main()
