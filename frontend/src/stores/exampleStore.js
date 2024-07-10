import { defineStore } from 'pinia'

// You can name the return value of `defineStore()` anything you want,
// but it's best to use the name of the store and surround it with `use`
// and `Store` (e.g. `useUserStore`, `useCartStore`, `useProductStore`)
// the first argument is a unique id of the store across your application

// You can think of state as the data of the store,
// getters as the computed properties of the store,
// and actions as the methods.

export const useCounterStore = defineStore('counter', {
  state: () => ({
    count: 0,
    name: 'Eduardo'
  }),
  getters: {
    doubleCount: state => state.count * 2
  },
  actions: {
    increment () {
      this.count++
    }
  }
})
