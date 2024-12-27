<script>
  import { Route, Router } from "svelte-routing";
  import Login from "./lib/Login.svelte";
  import Navigate from "./shared/Navigate.svelte";
  import Display from "./lib/Display.svelte";
</script>

<Router>
  <Route path="*">
    <Navigate to="/" />
  </Route>

  <Route path="/">
    <Login />
  </Route>

  <Route path="/display">
    <Display />
  </Route>
</Router>
