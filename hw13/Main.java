import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;

public class Main {
    private static HashMap<String, Integer> map = new HashMap<>();
    private static HashMap<String, Boolean> books = new HashMap<>();
    private static String lastTime = "[2023-01-01]";
    private static HashMap<String, ArrayList<String>> students = new HashMap<>();
    private static HashMap<String, ArrayList<String>> orders = new HashMap<>();
    private static HashMap<String, HashMap<String, Boolean>> goodBook = new HashMap<>();
    private static ArrayList<String> ids;
    private static ArrayList<String> library;

    public static void main(String[] args) throws ParseException {
        int times = (int) (Math.random() * 0 + 10);
        System.out.printf("3\nBUAA ");
        System.out.println(times);
        for (int i = 0; i < times; i++) {
            int type = 'A' + (int) (Math.random() * 2) + 1;
            int index = (int) (Math.random() * 9999);
            String book = String.format("%c", type) + "-" +
                    String.format("%04d", index);
            while (books.containsKey(book)) {
                type = 'A' + (int) (Math.random() * 2) + 1;
                index = (int) (Math.random() * 9999);
                book = String.format("%c", type) + "-" +
                        String.format("%04d", index);
            }
            books.put(book, true);
            int book_num = (int) (Math.random() * 4 + 1);
            map.put(book, book_num);
            ArrayList<String> order = new ArrayList<>();
            orders.put(book, order);
            if (Math.random() < 0.7) {
                System.out.println(book + " " +
                        book_num + " Y");
            } else {
                System.out.println(book + " " +
                        book_num + " N");
            }
        }
        System.out.println("PKE 0");
        System.out.println("THE 0");
        for (int i = 0; i < times / 3; i++) {
            int id = (int) (Math.random() * 99999998 + 1);
            String stu;
            if (Math.random() < 0.33) {
                stu = String.format("BUAA-%08d", id);
            } else if (Math.random() > 0.66) {
                stu = String.format("PKE-%08d", id);
            } else {
                stu = String.format("THE-%08d", id);
            }
            if (!students.containsKey(stu)) {
                ArrayList<String> books = new ArrayList<>();
                HashMap<String, Boolean> goods = new HashMap<>();
                students.put(stu, books);
                goodBook.put(stu, goods);
            } else {
                times--;
            }
        }
        library = new ArrayList<>(map.keySet());
        ids = new ArrayList<>(students.keySet());
        int ops = 5 * times;
        System.out.println(ops);
        SimpleDateFormat sdf = new SimpleDateFormat("[yyyy-MM-dd]");
        for (int i = 0; i < ops; i++) {
            Date d1 = sdf.parse(lastTime);
            d1.setTime(d1.getTime() + ((int) (Math.random() * 2 * 3600 * 24 * 1000)));
            if (Math.random() >= 0.95) {
                d1.setTime(d1.getTime() + ((int) (Math.random() * 3 * 3600 * 24 * 1000)));
            }
            String present = sdf.format(d1);
            System.out.println(getOp(present));
            lastTime = present;
        }
    }


    private static String getStu() {
        return ids.get((int) (Math.random() * ids.size()));
    }

    private static String getOp(String present) {
        int orders = (int) (Math.random() * 3) + 1;
        if (orders == 1) {
            String stu = getStu();
            if (!checkEmpty(stu)) {
                String book = getSmearedBook(stu);
                if (!checkSmeared(stu, book)) {
                    return String.format(present + " " + stu + " smeared " + book);
                } else {
                    return String.format(present + " " + stu + " borrowed " + getBook(stu));
                }
            } else {
                return String.format(present + " " + stu + " borrowed " + getBook(stu));
            }
        } else if (orders == 2) {
            String stu = getStu();
            if (!checkEmpty(stu)) {
                String book = LostBook(stu);
                if (!checkSmeared(stu, book)) {
                    return String.format(present + " " + stu + " lost " + book);
                } else {
                    return String.format(present + " " + stu + " borrowed " + getBook(stu));
                }
            } else {
                return String.format(present + " " + stu + " borrowed " + getBook(stu));
            }
        } else {
            String stu = getStu();
            if (!checkEmpty(stu)) {
                String book = getReturnBook(stu);
                return String.format(present + " " + stu + " returned " + book);
            } else {
                return String.format(present + " " + stu + " borrowed " + getBook(stu));
            }
        }
    }

    private static boolean checkSmeared(String stu, String book) {
        return (!goodBook.get(stu).get(book)) && students.get(stu).contains(book);
    }

    private static String LostBook(String stu) {
        String book = students.get(stu).get((int) (Math.random() * (students.get(stu).size())));
        students.get(stu).remove(book);
        goodBook.get(stu).put(book, true);
        return book;
    }

    private static boolean checkEmpty(String stu) {
        return students.get(stu).isEmpty();
    }

    private static String getReturnBook(String stu) {
        String book = students.get(stu).get((int) (Math.random() * (students.get(stu).size())));
        students.get(stu).remove(book);
        goodBook.get(stu).remove(book);
        if (orders.get(book).isEmpty()) {
            map.put(book, map.get(book) + 1);
        } else {
            String other = orders.get(book).get(0);
            students.get(other).add(book);
        }
        return book;
    }

    private static String getSmearedBook(String stu) {
        String book = students.get(stu).get((int) (Math.random() * (students.get(stu).size())));
        goodBook.get(stu).put(book, true);
        return book;
    }

    private static String getBook(String stu) {
        String book = library.get((int) (Math.random() * (library.size())));
        while (students.get(stu).contains(book)) {
            book = library.get((int) (Math.random() * (library.size())));
        }
        if (map.get(book) >= 1) {
            students.get(stu).add(book);
            map.put(book, map.get(book) - 1);
        } else {
            orders.get(book).add(stu);
        }
        goodBook.get(stu).put(book, false);
        return book;
    }
}
