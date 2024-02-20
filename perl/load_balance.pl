sub custom_load_balance {
    my @servers = ('server1:8000', 'server2:8000', 'server3:8000');
    my @weights = (3, 2, 1);  # Adjust weights as needed

    my $total_weight = 0;
    $total_weight += $_ for @weights;

    my $random_value = rand($total_weight);
    my $selected_server;
    my $current_weight = 0;

    for (my $i = 0; $i < @servers; $i++) {
        $current_weight += $weights[$i];
        if ($random_value < $current_weight) {
            $selected_server = $servers[$i];
            last;
        }
    }

    return $selected_server;
}
