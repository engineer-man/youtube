#include <stdio.h>
#include <stdlib.h>

typedef struct node_t {
    int data; // could be a struct to hold more data
    struct node_t *next;
} node_t;

node_t *head = NULL;

void add_at(int pos, int data) {
    node_t *node = malloc(sizeof(node_t) * 1);
    node->data = data;
    node->next = NULL;

    // handle case where list is empty
    if (head == NULL) {
        head = node;
        return;
    }

    int idx = 0;

    node_t *prev = NULL;
    node_t *cur = head;

    // walk through list until pos or end is reached
    while (cur != NULL && idx != pos) {
        ++idx;
        prev = cur;
        cur = cur->next;
    }

    // insertion point reached

    // beginning, includes head update
    if (idx == 0) {
        head = node;
        node->next = cur;
        return;
    }

    // end
    if (cur == NULL) {
        prev->next = node;
        return;
    }

    // middle
    prev->next = node;
    node->next = cur;
}

void add_beg(int data) {
    add_at(0, data);
}

void add_end(int data) {
    add_at(-1, data);
}

void rem(int data) {
    node_t *prev = NULL;
    node_t *cur = head;

    while (cur != NULL && cur->data != data) {
        prev = cur;
        cur = cur->next;
    }

    // null cur means no match, do nothing
    if (cur == NULL) {
        return;
    }

    // handle first item
    if (prev == NULL) {
        if (cur->next == NULL) {
            // only item?
            head = NULL;
        } else {
            // more items?
            head = cur->next;
        }

        free(cur);
        return;
    }

    // handle last item
    if (cur->next == NULL) {
        prev->next = NULL;

        free(cur);
        return;
    }

    // handle middle item
    if (prev != NULL && cur->next != NULL) {
        prev->next = cur->next;

        free(cur);
        return;
    }
}

void dump() {
    node_t *temp = head;

    while (temp != NULL) {
        printf("data: %d\n", temp->data);
        temp = temp->next;
    }
}

int main(int argc, char **argv) {
    add_end(2);
    add_end(3);
    add_end(5);
    add_beg(1);
    add_at(3, 4);

    printf("first:\n");
    dump();

    rem(1);
    rem(3);
    rem(5);

    printf("second:\n");
    dump();

    return 0;
}
