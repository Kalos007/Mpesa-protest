public class CustomArray {
    private int[] data;
    private int size;

    public CustomArray(int capacity) {
        data = new int[capacity];
        size = 0;
    }

    public void add(int value) {
        if (size == data.length) {
            resize();
        }
        data[size] = value;
        size++;
    }

    private void resize() {
        int[] newData = new int[data.length * 2];
        for (int i = 0; i < data.length; i++) {
            newData[i] = data[i];
        }
        data = newData;
    }

    public int get(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index is out of bounds");
        }
        return data[index];
    }

    public void print() {
        for (int i = 0; i < size; i++) {
            System.out.println(data[i]);
        }
    }

    public int size() {
        return size;
    }

    public static void main(String[] args) {
        CustomArray customArray = new CustomArray(3);
        customArray.add(10);
        customArray.add(20);
        customArray.add(30);
        customArray.add(40); // This will trigger resize

        customArray.print(); // Should print: 10, 20, 30, 40
    }
}
