#https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
#1047
using System.Collections;

public class Solution {
    public string RemoveDuplicates(string s) {
        string final_string = "";
        Stack<char> myStack = new Stack<char>();
        myStack.Push(s[0]);
        
        for(int i=1; i<s.Length; i++)
        {
            if(myStack.Count != 0)
            {
                if(s[i] == myStack.Peek())
                {
                    myStack.Pop();
                }
                else
                {
                    myStack.Push(s[i]);
                }
            }
            else
            {
                myStack.Push(s[i]);
            }
        }
        
        Stack<char> myStack1 = new Stack<char>();
        
        while(myStack.Count != 0)
        {
            myStack1.Push(myStack.Pop());
        }
        
        while(myStack1.Count != 0)
        {
            final_string += myStack1.Pop();
        }
        
        return final_string;
    }
}
