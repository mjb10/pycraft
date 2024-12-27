<script lang="ts">
    import { onMount } from "svelte";
    import { navigate } from "svelte-routing";
    import type { NavigateProps } from "@/types/Navigate";

    let { to }: NavigateProps = $props();

    onMount(() => {
        navigate(to);
    });
</script>
