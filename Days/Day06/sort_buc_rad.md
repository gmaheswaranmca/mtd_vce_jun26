# Radix Sort

## Idea

Radix Sort sorts numbers digit by digit.

* Start from the least significant digit (units place).
* Sort all numbers according to that digit.
* Move to tens place, hundreds place, and so on.
* Uses a stable sorting algorithm (usually Counting Sort) for each digit.

### Example

```text
Input:
170 45 75 90 802 24 2 66

After sorting by 1's digit:
170 90 802 2 24 45 75 66

After sorting by 10's digit:
802 2 24 45 66 170 75 90

After sorting by 100's digit:
2 24 45 66 75 90 170 802
```

---

## Algorithm

1. Find the maximum element.
2. Set `exp = 1`.
3. Perform Counting Sort using current digit `(number / exp) % 10`.
4. Multiply `exp` by 10.
5. Repeat until `max / exp > 0`.

---

## Pseudocode

```text
FUNCTION CountingSort(arr, exp)

    CREATE output[n]
    CREATE count[10] initialized to 0

    FOR each element
        digit ← (arr[i] / exp) MOD 10
        count[digit]++

    FOR i ← 1 TO 9
        count[i] ← count[i] + count[i-1]

    FOR i ← n-1 DOWNTO 0
        digit ← (arr[i] / exp) MOD 10
        output[count[digit]-1] ← arr[i]
        count[digit]--

    COPY output TO arr

END FUNCTION


FUNCTION RadixSort(arr)

    maxVal ← maximum element

    exp ← 1

    WHILE maxVal / exp > 0

        CountingSort(arr, exp)

        exp ← exp × 10

    END WHILE

END FUNCTION
```

---

## Complexity

| Case    | Complexity |
| ------- | ---------- |
| Best    | O(d × n)   |
| Average | O(d × n)   |
| Worst   | O(d × n)   |
| Space   | O(n + 10)  |

Where:

* n = number of elements
* d = number of digits

---

## C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

void countingSort(vector<int>& arr, int exp)
{
    int n = arr.size();

    vector<int> output(n);
    int count[10] = {0};

    for(int i = 0; i < n; i++)
        count[(arr[i] / exp) % 10]++;

    for(int i = 1; i < 10; i++)
        count[i] += count[i - 1];

    for(int i = n - 1; i >= 0; i--)
    {
        int digit = (arr[i] / exp) % 10;
        output[count[digit] - 1] = arr[i];
        count[digit]--;
    }

    arr = output;
}

void radixSort(vector<int>& arr)
{
    int maxVal = arr[0];

    for(int x : arr)
        if(x > maxVal)
            maxVal = x;

    for(int exp = 1; maxVal / exp > 0; exp *= 10)
        countingSort(arr, exp);
}

int main()
{
    int n;
    cin >> n;

    vector<int> arr(n);

    for(int i = 0; i < n; i++)
        cin >> arr[i];

    radixSort(arr);

    for(int x : arr)
        cout << x << " ";

    return 0;
}
```

---

## Java

```java
import java.util.*;

public class Main
{
    static void countingSort(int[] arr, int exp)
    {
        int n = arr.length;

        int[] output = new int[n];
        int[] count = new int[10];

        for(int i = 0; i < n; i++)
            count[(arr[i] / exp) % 10]++;

        for(int i = 1; i < 10; i++)
            count[i] += count[i - 1];

        for(int i = n - 1; i >= 0; i--)
        {
            int digit = (arr[i] / exp) % 10;
            output[count[digit] - 1] = arr[i];
            count[digit]--;
        }

        System.arraycopy(output, 0, arr, 0, n);
    }

    static void radixSort(int[] arr)
    {
        int maxVal = arr[0];

        for(int x : arr)
            maxVal = Math.max(maxVal, x);

        for(int exp = 1; maxVal / exp > 0; exp *= 10)
            countingSort(arr, exp);
    }

    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int[] arr = new int[n];

        for(int i = 0; i < n; i++)
            arr[i] = sc.nextInt();

        radixSort(arr);

        for(int x : arr)
            System.out.print(x + " ");
    }
}
```

---

## Python

```python
def counting_sort(arr, exp):
    n = len(arr)

    output = [0] * n
    count = [0] * 10

    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    arr[:] = output


def radix_sort(arr):
    max_val = max(arr)

    exp = 1

    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


n = int(input())
arr = list(map(int, input().split()))

radix_sort(arr)

print(*arr)
```

---

# Bucket Sort

## Idea

Bucket Sort distributes elements into buckets.

* Create multiple buckets.
* Put each element into a bucket.
* Sort each bucket individually.
* Merge buckets.

Works best when data is uniformly distributed.

---

## Example

```text
Input:
0.78 0.17 0.39 0.26 0.72 0.94 0.21

Bucket 0:
0.17 0.21 0.26

Bucket 1:
0.39

Bucket 2:
(empty)

Bucket 3:
(empty)

Bucket 4:
(empty)

Bucket 5:
(empty)

Bucket 6:
(empty)

Bucket 7:
0.72 0.78

Bucket 8:
(empty)

Bucket 9:
0.94

Output:
0.17 0.21 0.26 0.39 0.72 0.78 0.94
```

---

## Algorithm

1. Create n buckets.
2. Place elements into appropriate buckets.
3. Sort each bucket.
4. Concatenate buckets.

---

## Pseudocode

```text
FUNCTION BucketSort(arr)

    n ← length(arr)

    CREATE buckets[n]

    FOR each value x

        index ← floor(n × x)

        INSERT x INTO buckets[index]

    END FOR

    FOR each bucket

        SORT bucket

    END FOR

    MERGE all buckets into arr

END FUNCTION
```

---

## Complexity

| Case    | Complexity |
| ------- | ---------- |
| Best    | O(n)       |
| Average | O(n + k)   |
| Worst   | O(n²)      |
| Space   | O(n + k)   |

Where:

* n = elements
* k = buckets

---

## C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void bucketSort(vector<float>& arr)
{
    int n = arr.size();

    vector<vector<float>> buckets(n);

    for(float x : arr)
    {
        int idx = n * x;
        buckets[idx].push_back(x);
    }

    int k = 0;

    for(int i = 0; i < n; i++)
    {
        sort(buckets[i].begin(), buckets[i].end());

        for(float x : buckets[i])
            arr[k++] = x;
    }
}

int main()
{
    int n;
    cin >> n;

    vector<float> arr(n);

    for(int i = 0; i < n; i++)
        cin >> arr[i];

    bucketSort(arr);

    for(float x : arr)
        cout << x << " ";

    return 0;
}
```

---

## Java

```java
import java.util.*;

public class Main
{
    static void bucketSort(float[] arr)
    {
        int n = arr.length;

        ArrayList<Float>[] buckets = new ArrayList[n];

        for(int i = 0; i < n; i++)
            buckets[i] = new ArrayList<>();

        for(float x : arr)
        {
            int idx = (int)(n * x);
            buckets[idx].add(x);
        }

        int k = 0;

        for(int i = 0; i < n; i++)
        {
            Collections.sort(buckets[i]);

            for(float x : buckets[i])
                arr[k++] = x;
        }
    }

    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        float[] arr = new float[n];

        for(int i = 0; i < n; i++)
            arr[i] = sc.nextFloat();

        bucketSort(arr);

        for(float x : arr)
            System.out.print(x + " ");
    }
}
```

---

## Python

```python
def bucket_sort(arr):
    n = len(arr)

    buckets = [[] for _ in range(n)]

    for x in arr:
        index = int(n * x)
        buckets[index].append(x)

    k = []

    for bucket in buckets:
        bucket.sort()
        k.extend(bucket)

    return k


n = int(input())
arr = list(map(float, input().split()))

result = bucket_sort(arr)

print(*result)
```

## Input

```text
7
0.78 0.17 0.39 0.26 0.72 0.94 0.21
```

## Output

```text
0.17 0.21 0.26 0.39 0.72 0.78 0.94
```
