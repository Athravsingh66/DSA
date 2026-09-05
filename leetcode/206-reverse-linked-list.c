// Question
// LeetCode 206 - Reverse Linked List


// Solution

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* ptr=head;
    struct ListNode* prev=NULL;
    while (ptr!=NULL)
    {
        struct ListNode* next=ptr->next;
        ptr->next=prev;
        prev=ptr;
        ptr=next;
    }    
    return prev;
}