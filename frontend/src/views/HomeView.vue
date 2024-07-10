<template>
  <main>
    <h1 class="text-blue-500">Hello World</h1>
    <button class="px-2 py-2 bg-cyan-500 hover:bg-cyan-600" @click="increment">Count is: {{ counterStore.count }}</button>
    <h3>{{ counterStore.doubleCount }}</h3>
  </main>
</template>

<script>
import { mapStores } from 'pinia';
import { useCounterStore } from '@/stores/exampleStore'

export default {
  computed: {
    // note we are not passing an array, just one store after the other
    // each store will be accessible as its id + 'Store'
    ...mapStores(useCounterStore)
  },
  data() {
    return {
    }
  },
  methods: {
    increment() {
      this.counterStore.increment()
    }
  },
  // `mounted` is a lifecycle hook which we will explain later
  mounted() {
  }
}

</script>