public class Main {
    
  public static int ShakerSort(int A[]) {
       int l = 0;
       int p = 0;
       int r = A.length-1;
       char d = 'a';
       while (l<r) {
           if (d == 'a') {
               for(int j=1; j<r; j++) {
                   if (A[j]>A[j+1]) {
                       int aux = A[j];
                      A[j] = A[j+1];
                      A[j] = A[j+1];
                      A[j+1] = aux;
                      p++;
                  }
              }
              r--;
              d = 'i';
          } else {
              for(int j=r; j>1; j--) {
                  if (A[j]<A[j-1]) {
                      int aux = A[j-1];
                      A[j] = A[j-1];
                      A[j-1] = aux;
                      p++;
                  }
              }
              l++;
              d = 'a';
          }
     }
     return p;
   }
   
   public static void main(String[] args) {
          int[] vettore = new int[10];
          for (int i = 0; i < vettore.length; i++) {
              vettore[i] = (int) (Math.random() * 51);
              if (vettore[i] == 51) {
                  vettore[i] = 50;
              }
          }
          System.out.println(ShakerSort(vettore));
      }
}
