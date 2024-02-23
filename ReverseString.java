public class ReverseString {
    public static String reverse (String st){
        
        char[] res =st.toCharArray();
        String reversed ="";
    
        for(int i= res.length-1;i>=0;i--)
        {
          reversed = reversed+res[i];
        }
       
        return reversed;
    }
    public static String reverseFunction (String st){
       StringBuilder str =  new StringBuilder();
       str.append(st);
       str.reverse();
       return str.toString();
    }
    public static void main(String[] args){
        String res = "harshita";
        String reverse = reverse(res);
        String rf = reverseFunction(res);
        System.out.println(reverse);
        System.out.println(rf);

    }
    
}
