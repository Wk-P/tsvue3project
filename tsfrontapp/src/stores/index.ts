// src/stores/index.ts
import { defineStore } from "pinia";
import { ref } from "vue";
import type { Item } from "@/types/index";

export const useItemStore = defineStore("item", () => {
    const item = ref<Item | null>(null);
    const setItem = (newItem: Item) => {
        item.value = newItem;
        localStorage.setItem("item", JSON.stringify(newItem)); // 保存到 localStorage
    };

    const clearItem = () => {
        item.value = null;
        localStorage.removeItem("item"); // 从 localStorage 移除
    };

    const loadItem = () => {
        const storedItem = localStorage.getItem("item");
        if (storedItem) {
            item.value = JSON.parse(storedItem);
        }
    };

    loadItem();

    return {
        item,
        setItem,
        clearItem,
    };
});

export const useSearchStore = defineStore("search", () => {
    const searchResultsList = ref<Array<Item> | null>(null);
    const setResults = (searchResults: Array<Item>) => {
        searchResultsList.value = searchResults;
        localStorage.setItem("searchResults", JSON.stringify(searchResults));
    };

    const clearResults = () => {
        searchResultsList.value = null;
        localStorage.removeItem("searchResults");
    };

    const loadResults = () => {
        const storedResults = localStorage.getItem("searchResults");
        if (storedResults) {
            searchResultsList.value = JSON.parse(storedResults);
        }
    };

    loadResults();

    return {
        searchResultsList,
        setResults,
        clearResults,
    };
});
