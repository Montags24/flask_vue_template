<template>
  <main>
    <h1 class="text-blue-500">Hello World</h1>
    <button class="px-2 py-2 bg-cyan-500 hover:bg-cyan-600" @click="increment">Count is: {{ count }}</button>
  </main>
</template>

<script>
export default {
  data() {
    return {
      count: 1
    }
  },
  methods: {
    increment() {
      this.count ++
    }
  },
  // `mounted` is a lifecycle hook which we will explain later
  mounted() {
    // `this` refers to the component instance.
    console.log(this.count) // => 1

    // data can be mutated as well
    this.count = 2
  }
}

</script>