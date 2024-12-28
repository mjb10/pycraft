<script>
  import { Route, Router } from "svelte-routing";
  import Login from "./lib/Login.svelte";
  import Navigate from "./shared/Navigate.svelte";
  import Display from "./lib/Display.svelte";

  import files from "./assets/importedFiles";

  files.forEach((file) => {
    const script = document.createElement("script");
    script.setAttribute("type", "mpy");
    script.setAttribute("src", file);
    document.body.appendChild(script);
  });
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
