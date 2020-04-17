import java.util.Objects;

public class Couple implements Contenant<Integer>{

    private Integer x,y;

    public Couple(Integer x, Integer y) {
        this.x = x;
        this.y = y;
    }

    public Couple() {
        this.x = 0;
        this.y = 0;
    }

    @Override
    public String toString() {
        return "Couple{" +
                "x=" + x +
                ", y=" + y +
                '}';
    }

    public Integer getX() {
        return x;
    }

    public void setX(Integer x) {
        this.x = x;
    }

    public Integer getY() {
        return y;
    }

    public void setY(Integer y) {
        this.y = y;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Couple couple = (Couple) o;
        return Objects.equals(x, couple.x) &&
                Objects.equals(y, couple.y);
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y);
    }

    @Override
    public boolean contient(Integer a) {
        return a == this.x || a == this.y;
    }
}
