import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Partition {

    private List<NotAcc> partition;

    public Partition (){
        this.partition = new ArrayList<>();
    }

    public List<NotAcc> getPartition() {
        return partition;
    }

    public void setPartition(List<NotAcc> partition) {
        this.partition = partition;
    }

    public void add (NotAcc x){
        this.partition.add(x);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Partition partition1 = (Partition) o;
        return partition.equals(partition1.partition);
    }

    public void jouer (){
        for (int i = 0; i < this.partition.size(); ++i){
            this.partition.get(i).jouer();
        }
    }
}
