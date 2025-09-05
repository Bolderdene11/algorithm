import unittest
import zipfile

def read_zip_file(zip_path, filename_inside_zip):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            if filename_inside_zip in zip_ref.namelist():
                with zip_ref.open(filename_inside_zip) as f:
                    content = f.read().decode('utf-8')
                    print("Файлын агуулга (zip дотор):")
                    print(content)
                    return content
            else:
                print(f"{filename_inside_zip} файл zip дотор олдсонгүй.")
    except FileNotFoundError:
        print(f"{zip_path} файл олдсонгүй.")
    except zipfile.BadZipFile:
        print(f"{zip_path} нь хүчинтэй zip файл биш байна.")
    except IOError as e:
        print(f"I/O алдаа: {e}")


def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            print(" Файлын агуулга:")
            print(content)
            return content
    except FileNotFoundError:
        print(f"{"C:\\Users\\Dell\\OneDrive\\Desktop\\algorithm\\shuleg.txt"}'файл олдсонгүй.")

    except IOError as e:
        print(f" IO алдаа: {e}")


def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def binary_search_recursive(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        mid = len(arr) // 2
        left_max = find_max(arr[:mid])
        right_max = find_max(arr[mid:])
        return max(left_max, right_max)


class TestAlgorithms(unittest.TestCase):

    def test_insertion_sort(self):
        lst = [12, 3, 7, 9, 14, 6, 11, 2]
        insertion_sort(lst)
        self.assertEqual(lst, [2, 3, 6, 7, 9, 11, 12, 14])

    def test_merge_sort(self):
        lst = [12, 3, 7, 9, 14, 6, 11, 2]
        merge_sort(lst)
        self.assertEqual(lst, [2, 3, 6, 7, 9, 11, 12, 14])

    def test_binary_search(self):
        sorted_list = [2, 3, 6, 7, 9, 11, 12, 14]
        index = binary_search_recursive(sorted_list, 9)
        self.assertEqual(index, 4)
        not_found = binary_search_recursive(sorted_list, 100)
        self.assertEqual(not_found, -1)

    def test_find_max(self):
        lst = [12, 3, 7, 9, 14, 6, 11, 2]
        self.assertEqual(find_max(lst), 14)


if __name__ == "__main__":
    read_file("C:\\Users\\Dell\\OneDrive\\Desktop\\algorithm\\shuleg.txt") 
    read_zip_file("C:\\Users\\Dell\\OneDrive\\Desktop\\algorithm\\hoosn .zip", "hoosn.txt")

    print("\n юнит тестүүд\n")
    unittest.main(argv=[''], verbosity=2, exit=False)
