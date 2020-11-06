public class Main {

public static void ShakerSort(int A[]) {
       int l = 0;
       boolean pane = false;
       int r = A.length-1;
       char d = 'a';
       while (l<r) {
           if (d == 'a') {
               for(int j=1; j<r; j++) {
                   if (A[j]<A[j+1]) {
                       int aux = A[j];
                      A[j] = A[j+1];
                      A[j] = A[j+1];
                      A[j+1] = aux;
                      pane = true;
                  }
              }
              if(!pane) break;
              r--;
              d = 'i';
          } else {
              for(int j=r; j>1; j--) {
                  if (A[j]>A[j-1]) {
                      int aux = A[j-1];
                      A[j] = A[j-1];
                      A[j-1] = aux;
                      pane = true;
                  }
              }
              if(!pane) break;
              l++;
              d = 'a';
          }
     }
   }
   
   public static void main(String[] args) {
          int[] vettore = new int[10];
          for (int i = 0; i < vettore.length; i++) {
              vettore[i] = (int) (Math.random() * 51);
              if (vettore[i] == 51) {
                  vettore[i] = 50;
              }
          }
          ShakerSort(vettore);
          for(int i=0;i<vettore.length;i++) {
              System.out.print(vettore[i]+" ");
          }
      }
}
