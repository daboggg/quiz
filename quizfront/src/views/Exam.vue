<template>
<h1>{{params}}</h1>
</template>

<script>
export default {
  name: "Exam",
  data:()=>({
    params:null
  }),
  created() {
    this.params = this.$route.query
  }
}
</script>

<style scoped>

</style>