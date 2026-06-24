/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if(!head || left == right)
            return head;
        
        ListNode* dummy = new ListNode(0, head);
        ListNode* beforeLeft = dummy;

        ListNode* cur = head;
        for(int i = 1; i < left; i++)
        {
            beforeLeft = cur;
            cur = cur->next;
        }

        ListNode* prev = nullptr;
        for(int i = 1; i <= right - left + 1; i++)
        {
            ListNode* tmp = cur->next;
            cur->next = prev;
            prev = cur;
            cur = tmp;
        }

        beforeLeft->next->next = cur;
        beforeLeft->next = prev;

        return dummy->next;


    }

};