#include <linux/kernel.h>       // Contains types, macros, functions for the kernel
#include <linux/module.h>       // Contains types, macros, functions for the module
#include <linux/netfilter.h>    // Contains types, macros, functions for netfilter
#include <linux/netfilter_ipv4.h> // Definitions for IP packet filtering
#include <linux/ip.h>           // Definitions for IP (Internet Protocol)
#include <linux/tcp.h>          // Definitions for TCP (Transmission Control Protocol)

// Declare a Netfilter hook operations structure
static struct nf_hook_ops telnetFilterHook;

// Function to filter telnet packets
unsigned int telnetFilter(void *priv, struct sk_buff *skb,
                            const struct nf_hook_state *state)
{
    struct iphdr *iph;  // IP header structure
    struct tcphdr *tcph; // TCP header structure

    // Get IP header from packet
    iph = ip_hdr(skb);
    // Get TCP header from packet
    tcph = (void *)iph+iph->ihl*4;

    // Check if packet is TCP and destination port is 23 (telnet)
    if (iph->protocol == IPPROTO_TCP && tcph->dest == htons(23)) {
        // Print message and drop packet if it's a telnet packet
        printk(KERN_INFO "Dropping telnet packet to %pI4\n", &iph->daddr);
        return NF_DROP;
    } else {
        // Accept packet if it's not a telnet packet
        return NF_ACCEPT;
    }
}

// Function to set up the Netfilter hook
int setupFilter(void) {
    printk(KERN_INFO "Registering a telnet filter.\n");

    // Set the hook function. This function will be called for each packet.
    telnetFilterHook.hook = telnetFilter;

    // Set the hook number. NF_INET_POST_ROUTING is the point where the hook is placed in the network stack.
    telnetFilterHook.hooknum = NF_INET_POST_ROUTING;

    // Set the protocol family. PF_INET is the protocol family for IPv4.
    telnetFilterHook.pf = PF_INET;

    // Set the priority of the hook. NF_IP_PRI_FIRST means this hook will be called first.
    telnetFilterHook.priority = NF_IP_PRI_FIRST;

    // Register the hook
    nf_register_net_hook(&telnetFilterHook);
    return 0;
}

// Function to remove the Netfilter hook
void removeFilter(void) {
    printk(KERN_INFO "Telnet filter is being removed.\n");
    nf_unregister_net_hook(&telnetFilterHook);
}

// Specify the function to call when the module is loaded
module_init(setupFilter);

// Specify the function to call when the module is removed
module_exit(removeFilter);

// Specify the license for the module
MODULE_LICENSE("GPL");