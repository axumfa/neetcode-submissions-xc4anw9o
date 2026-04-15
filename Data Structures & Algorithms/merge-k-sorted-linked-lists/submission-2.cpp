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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(lists.size() == 0)
            return nullptr;
        
        while(lists.size() > 1)
        {
            vector<ListNode*> mergedList;
            int size = lists.size();

            for(int i = 0; i < size; i += 2)
            {
                ListNode* l1 = lists[i];
                ListNode* l2 = nullptr;
                if( i + 1 < size)
                {
                    l2 = lists[i + 1];
                }
                mergedList.push_back(mergeList(l1, l2));

            }
            lists = mergedList;
        }
        return lists[0];

    }

    ListNode* mergeList(ListNode* l1, ListNode* l2)
    {
        ListNode* dummy = new ListNode(0);
        ListNode* cur = dummy;

        while(l1 != nullptr && l2 != nullptr)
        {
            if(l1->val > l2->val)
            {
                cur->next = l2;
                l2 = l2->next;
            }
            else
            {
                cur->next = l1;
                l1 = l1->next;
            }
            cur = cur->next;
        }
        cur->next = (l1 ? l1 : l2);

        return dummy->next;
    }
};
