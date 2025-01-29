import requests
import json
import time

def send_request_to_cloudflare_getcode(url, method="POST", data=None, headers=None, timeout=10):
    """
    این تابع یک درخواست به URL مشخص شده ارسال می‌کند.

    Args:
        url: آدرس کامل URL مقصد.
        method: متد HTTP (POST, GET, PUT, DELETE و غیره). پیش‌فرض POST است.
        data: داده‌هایی که در بدنه درخواست ارسال می‌شوند (به صورت دیکشنری یا رشته JSON).
        headers: هدرهای درخواست (به صورت دیکشنری).
        timeout: مدت زمان Timeout درخواست به ثانیه.

    Returns:
        یک تاپل شامل پاسخ (به صورت دیکشنری یا متن)، کد وضعیت HTTP و زمان صرف شده برای درخواست.
        در صورت بروز خطا، یک دیکشنری شامل پیام خطا و کد وضعیت 500 برگردانده می‌شود.
    """
    start_time = time.time()
    try:
        if headers is None:
            headers = {'Content-Type': 'application/json'} # هدر پیش فرض برای درخواست های json

        if data and isinstance(data, dict):
            data = json.dumps(data) # تبدیل دیکشنری به JSON در صورت نیاز

        response = requests.request(method, url, data=data, headers=headers, timeout=timeout)
        response.raise_for_status()  # بررسی کد وضعیت و ایجاد خطا برای کدهای 4xx و 5xx

        try:
            response_json = response.json()
            return response_json, response.status_code, time.time() - start_time
        except json.JSONDecodeError:
            return response.text, response.status_code, time.time() - start_time

    except requests.exceptions.Timeout:
        error_message = f"Request to {url} timed out after {timeout} seconds."
        print(f"Error: {error_message}")
        return {"error": error_message}, 500, time.time() - start_time
    except requests.exceptions.ConnectionError as e:
        error_message = f"Connection error to {url}: {e}"
        print(f"Error: {error_message}")
        return {"error": error_message}, 500, time.time() - start_time
    except requests.exceptions.RequestException as e:
        error_message = f"Request error to {url}: {e}"
        print(f"Error: {error_message}")
        if response is not None:
            print(f"Response text: {response.text}")
        return {"error": error_message, "response_text": response.text if response is not None else None}, response.status_code if response is not None else 500, time.time() - start_time
    except Exception as e:
        error_message = f"An unexpected error occurred: {e}"
        print(f"Error: {error_message}")
        return {"error": error_message}, 500, time.time() - start_time
    finally:
        elapsed_time = time.time() - start_time
        print(f"Total request time: {elapsed_time:.4f} seconds")


# if __name__ == "__main__":
#     worker_url = "https://fletorder.bbcd3146.workers.dev/send-sms" # گرفتن آدرس Worker از متغیر محیطی
#     if not worker_url:
#         print("Error: WORKER_URL environment variable is not set.")
#         exit()

    test_data = {"mobile_number": "09170718627"} # داده های ارسالی به Worker
    test_headers = {"x-verification-code": "123456"} # هدر های ارسالی به Worker

    response, status_code, elapsed_time = send_request_to_cloudflare(worker_url, data=test_data, headers=test_headers)

    print(f"Request to: {worker_url}")
    print(f"Status Code: {status_code}")
    print(f"Response Time: {elapsed_time:.4f} seconds")

    if status_code == 200:
        print("Response:")
        print(json.dumps(response, indent=4, ensure_ascii=False)) # چاپ پاسخ با فرمت خوانا
    else:
        print("Error details:")
        print(json.dumps(response, indent=4, ensure_ascii=False))





def send_request_to_cloudflare_verify(method="POST", mobile_number=None, verify_code=None, timeout=10):
    """
    این تابع یک درخواست به URL مشخص شده ارسال می‌کند.

    Args:
        url: آدرس کامل URL مقصد.
        method: متد HTTP (POST, GET, PUT, DELETE و غیره). پیش‌فرض POST است.
        data: داده‌هایی که در بدنه درخواست ارسال می‌شوند (به صورت دیکشنری یا رشته JSON).
        headers: هدرهای درخواست (به صورت دیکشنری).
        timeout: مدت زمان Timeout درخواست به ثانیه.

    Returns:
        یک تاپل شامل پاسخ (به صورت دیکشنری یا متن)، کد وضعیت HTTP و زمان صرف شده برای درخواست.
        در صورت بروز خطا، یک دیکشنری شامل پیام خطا و کد وضعیت 500 برگردانده می‌شود.
    """
    worker_url = "https://fletorder.bbcd3146.workers.dev/verify-code" # گرفتن آدرس Worker از متغیر محیطی
    if not worker_url:
        print("Error: WORKER_URL environment variable is not set.")
        exit()
    test_data = {"mobile_number": mobile_number,"verification_code":verify_code+'.0'} # داده های ارسالی به Worker
    test_headers = {"x-verification-code": "123456"} # هدر های ارسالی به Worker    
    start_time = time.time()
    try:
        if headers is None:
            headers = {'Content-Type': 'application/json'} # هدر پیش فرض برای درخواست های json

        if data and isinstance(data, dict):
            data = json.dumps(data) # تبدیل دیکشنری به JSON در صورت نیاز

        response = requests.request(method, worker_url, data=test_data, headers=test_headers, timeout=timeout)
        response.raise_for_status()  # بررسی کد وضعیت و ایجاد خطا برای کدهای 4xx و 5xx

        try:
            response_json = response.json()
            return response_json, response.status_code, time.time() - start_time
        except json.JSONDecodeError:
            return response.text, response.status_code, time.time() - start_time

    except requests.exceptions.Timeout:
        error_message = f"Request to {url} timed out after {timeout} seconds."
        print(f"Error: {error_message}")
        return {"error": error_message}, 500, time.time() - start_time
    except requests.exceptions.ConnectionError as e:
        error_message = f"Connection error to {url}: {e}"
        print(f"Error: {error_message}")
        return {"error": error_message}, 500, time.time() - start_time
    except requests.exceptions.RequestException as e:
        error_message = f"Request error to {url}: {e}"
        print(f"Error: {error_message}")
        if response is not None:
            print(f"Response text: {response.text}")
        return {"error": error_message, "response_text": response.text if response is not None else None}, response.status_code if response is not None else 500, time.time() - start_time
    except Exception as e:
        error_message = f"An unexpected error occurred: {e}"
        print(f"Error: {error_message}")
        return {"error": error_message}, 500, time.time() - start_time
    finally:
        elapsed_time = time.time() - start_time
        print(f"Total request time: {elapsed_time:.4f} seconds")


if __name__ == "__main__":
    worker_url = "https://fletorder.bbcd3146.workers.dev/verify-code" # گرفتن آدرس Worker از متغیر محیطی
    if not worker_url:
        print("Error: WORKER_URL environment variable is not set.")
        exit()

    test_data = {"mobile_number": "09170718627","verification_code": "32832.0"} # داده های ارسالی به Worker
    test_headers = {"x-verification-code": "123456"} # هدر های ارسالی به Worker

    response, status_code, elapsed_time = send_request_to_cloudflare_verify(worker_url, data=test_data, headers=test_headers)

    print(f"Request to: {worker_url}")
    print(f"Status Code: {status_code}")
    print(f"Response Time: {elapsed_time:.4f} seconds")

    if status_code == 200:
        print("Response:")
        print(json.dumps(response, indent=4, ensure_ascii=False)) # چاپ پاسخ با فرمت خوانا
    else:
        print("Error details:")
        print(json.dumps(response, indent=4, ensure_ascii=False))