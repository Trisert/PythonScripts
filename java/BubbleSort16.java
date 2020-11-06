public class Main {

    public static void BubbleSort(int[]A) {
        int c=0;
        boolean s;
        int i= A.length-1;
        int flag=0;
        while(i>0) {
            s=false;
            c++;
            for (int j=0; j<i; j++) {
                if (A[j]>A[j+1]) {
                    int aux = A[j];
                    A[j] = A[j+1];
                    A[j+1] = aux;
                    s = true;
                    flag=0;
                } else {
                    flag++;
                }
                if(j==i-1&&flag!=0) {
                    i=i-flag+1;
                }
              }
            i--;
            if(!s) {
                break;
            }
        }
        for(int x=0; x<A.length; x++) {
            System.out.print(" "+A[x]+" ");
        }
    }

    public static void main(String[]args) {
        int[] A= {6,8,3,4,1,5};
        BubbleSort(A);
    }
}
